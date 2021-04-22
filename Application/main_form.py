import cv2
import numpy as np
import json
import re
import io
import contextlib
import os
import math

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QListWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt

from main_form_designer import Ui_MainWindow
from ImageProcessing.image_process import ImageProcess
from RobotInteraction.contours import FindContours
from RobotInteraction.robot_control import FindInitPosition, Draw, Hatch, Stop


class CobArt(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('Data/Resource/byAlex.ico'))
        self.setupUi(self)

        # Objects and Data
        self.image_process = ImageProcess()
        self.method_parameters = self._GetConfiguration()

        # Buttons
        self.buttonLoadImage.clicked.connect(self._ButtonLoadImageClicked)
        self.buttonPhoto.clicked.connect(self._ButtonPhotoClicked)
        self.buttonSaveImage.clicked.connect(self._ButtonSaveImageClicked)
        self.buttonApply.clicked.connect(self._ButtonApplyClicked)
        self.buttonRemove.clicked.connect(self._ButtonRemoveClicked)
        self.buttonClear.clicked.connect(self._ButtonClearClicked)
        self.buttonFindInitPosition.clicked.connect(self._FindInitPosition)
        self.buttonDraw.clicked.connect(self._Draw)
        self.buttonStop.clicked.connect(self._Stop)

        # ComboBoxes
        self.command_list = {'Blur': ["Average", "Bilateral", "Gaussian", "Median"],
                             'Kernel': ["Sharpen", "My Variant"],
                             'Edge Detection': ["Canny", "Laplacian", "Sobel X", "Sobel Y", "Sobel", "Scharr X",
                                                "Scharr Y", "Simple Thresholding", "Adaptive Thresholding"],
                             'Morphology': ["Dilate", "Erode", "Close", "Open", "Gradient"]}
        self.comboBoxCategory.addItems(self.command_list.keys())
        self._SetComboboxItems(category=self.comboBoxCategory.currentText())
        self.comboBoxCategory.currentTextChanged.connect(self._ComboboxCategoryChanged)
        self.comboBoxType.currentTextChanged.connect(self._ComboboxTypeChanged)

        self.approx_list = ["Simple", "TC89_KCOS", "TC89_L1"]
        self.comboBoxApprox.addItems(self.approx_list)
        self.comboBoxApprox.currentTextChanged.connect(self._FindContours)

        # SpinBoxes
        self.spinBoxThreshold.valueChanged.connect(self._FindContours)
        self.spinBoxArea.valueChanged.connect(self._FindContours)
        self.comboBoxType.activated[str].connect(self._SetAccessKernelSpinBoxes)
        self._HideAllSpinBoxes()
        self._SetSpinBoxes(self.method_parameters[self.comboBoxCategory.currentText()]
                            [self.comboBoxType.currentText()])

    # IMAGE PROCESSING EVENTS
    def _ButtonLoadImageClicked(self):
        self.image_path = QFileDialog.getOpenFileName(filter='Изображения (*.jpg *.jpeg *.png)')
        self.image_path = self.image_path[0]
        if len(self.image_path) > 0:
            self.image_process.image = cv2.imread(self.image_path)
            self.image_process.original_image = self.image_process.image
            cv2.imwrite('Data/Temp/Original.jpg', self.image_process.original_image)
            self._SetImagePictureBoxOriginal('Data/Temp/Original.jpg')
            self._SetImagePictureBoxOutput('Data/Temp/Original.jpg')
            self._SetImagePictureBoxOutput2('Data/Temp/Original.jpg')
            self.listBoxImages.clear()
        else:
            return

    def _ButtonPhotoClicked(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret, frame = camera.read()
            cv2.imshow('Press "q" to take a photo', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.listBoxImages.clear()
                self.image_process.image = frame
                self.image_process.original_image = frame
                cv2.imwrite('Data/Temp/Original.jpg', self.image_process.original_image)
                self._SetImagePictureBoxOriginal('Data/Temp/Original.jpg')
                self._SetImagePictureBoxOutput('Data/Temp/Original.jpg')
                self._SetImagePictureBoxOutput2('Data/Temp/Original.jpg')
                break
        camera.release()
        cv2.destroyAllWindows()

    def _ButtonSaveImageClicked(self):
        self.image_process.image = cv2.imread(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self.image_path = QFileDialog.getSaveFileName(filter='JPG (*.jpg);; PNG (*.png)')
        self.image_path = self.image_path[0]
        if len(self.image_path) > 0:
            cv2.imwrite(self.image_path, self.image_process.image)
        else:
            return

    def _ButtonApplyClicked(self):
        category = self.comboBoxCategory.currentText()
        name = self.comboBoxType.currentText()
        text, method = self._GetMethodInfo(self.comboBoxCategory.currentText(), self.comboBoxType.currentText(),
                                           self.method_parameters[self.comboBoxCategory.currentText()]
                                            [self.comboBoxType.currentText()])
        self.image_process.temp_images.append(method)
        self._ApplyMethod(category, name, len(self.image_process.temp_images) - 1)
        cv2.imwrite(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg', self.image_process.image)
        self._SetImagePictureBoxOutput(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self._SetImagePictureBoxOutput2(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self._SetListboxItem(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg', text)

    def _ButtonRemoveClicked(self):
        index = self.listBoxImages.currentRow()
        self.image_process.temp_images.pop(index)
        self.image_process.image = self.image_process.original_image
        self.listBoxImages.takeItem(index)
        for index in range(len(self.image_process.temp_images)):
            self._ApplyMethod(self.image_process.temp_images[index]['category'],
                              self.image_process.temp_images[index]['name'],
                              index)
            cv2.imwrite(f'Data/Temp/Temp{index}.jpg', self.image_process.image)
        if self.image_process.temp_images:
            self._SetImagePictureBoxOutput(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
            self._SetImagePictureBoxOutput2(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        else:
            self._SetImagePictureBoxOutput(f'Data/Temp/Original.jpg')
            self._SetImagePictureBoxOutput2(f'Data/Temp/Original.jpg')

    def _ButtonClearClicked(self):
        for index in range(len(self.image_process.temp_images)):
            os.remove(f'Data/Temp/Temp{index}.jpg')
            self.image_process.temp_images.clear()
        self.listBoxImages.clear()
        self.image_process.image = self.image_process.original_image
        self._SetImagePictureBoxOutput(f'Data/Temp/Original.jpg')
        self._SetImagePictureBoxOutput2(f'Data/Temp/Original.jpg')

    def _ComboboxCategoryChanged(self, value):
        self._SetComboboxItems(category=value)

    def _ComboboxTypeChanged(self, value):
        if self.comboBoxType.count() == 0:
            return
        self._HideAllSpinBoxes()
        self._SetSpinBoxes(self.method_parameters[self.comboBoxCategory.currentText()][value])

    def closeEvent(self, event):
        if len(self.image_process.temp_images) > 0:
            for i in range(len(self.image_process.temp_images)):
                os.remove(f'Data/Temp/Temp{i}.jpg')
        if os.path.exists('Data/Temp/Original.jpg'):
            os.remove('Data/Temp/Original.jpg')
        if os.path.exists('Data/Temp/Contours.jpg'):
            os.remove('Data/Temp/Contours.jpg')
        event.accept()

    # IMAGE PROCESSING FUNCTIONAL
    def _SetComboboxItems(self, category):
        self.comboBoxType.clear()
        self.comboBoxType.addItems(self.command_list[category])

    def _SetListboxItem(self, image_path, text):
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.listBoxImages.iconSize(), Qt.KeepAspectRatio)
        item = QListWidgetItem()
        item.setIcon(QIcon(self.pixmap))
        item.setText(self.comboBoxType.currentText())
        item.setToolTip(text)
        self.listBoxImages.addItem(item)

    def _SetImagePictureBoxOriginal(self, image_path):
        # Picture Box Original
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.pictureBoxOriginal.size(), Qt.KeepAspectRatio)
        self.pictureBoxOriginal.setAlignment(Qt.AlignCenter)
        self.pictureBoxOriginal.setPixmap(self.pixmap)

    def _SetImagePictureBoxOutput(self, image_path):
        self.pixmap = QPixmap(QImage(image_path))
        # Picture Box Output
        self.pixmap = self.pixmap.scaled(self.pictureBoxOutput.size(), Qt.KeepAspectRatio)
        self.pictureBoxOutput.setAlignment(Qt.AlignCenter)
        self.pictureBoxOutput.setPixmap(self.pixmap)
        # Picture Box Processed
        self.pixmap = self.pixmap.scaled(self.pictureBoxProcessed.size(), Qt.KeepAspectRatio)
        self.pictureBoxProcessed.setAlignment(Qt.AlignCenter)
        self.pictureBoxProcessed.setPixmap(self.pixmap)

    def _SetImagePictureBoxOutput2(self, image_path):
        # Picture Box Output 2
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.pictureBoxOutput2.size(), Qt.KeepAspectRatio)
        self.pictureBoxOutput2.setAlignment(Qt.AlignCenter)
        self.pictureBoxOutput2.setPixmap(self.pixmap)

    def _GetMethodInfo(self, category, name, parameters=dict):
        text = [category]
        method = {'category': category, 'name': name}
        for key in parameters.keys():
            if key[:len(key) - 1] == 'spinBox':
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    exec(f'print(self.{key}.value())')
                text.append(f"{parameters[key]['name']}: {stream.getvalue()}")
                method[parameters[key]['name']] = int(stream.getvalue())
        if category == "Kernel":
            text.append(f"matrix:\n {self._GetKernel()}")
            method['matrix'] = self._GetKernel()
        text = "; ".join(text)
        return text, method

    def _GetConfiguration(self):
        with open('Data/Parameters.json') as file:
            data = json.load(file)
        return data

    def _GetKernel(self):
        return np.array([[self.spinBoxKernel1.value(), self.spinBoxKernel2.value(), self.spinBoxKernel3.value()],
                         [self.spinBoxKernel4.value(), self.spinBoxKernel5.value(), self.spinBoxKernel6.value()],
                         [self.spinBoxKernel7.value(), self.spinBoxKernel8.value(), self.spinBoxKernel9.value()]])

    def _HideAllSpinBoxes(self):
        for i in range(1, 10):
            if i < 6:
                exec(f'self.label{i}.hide()')
                exec(f'self.spinBox{i}.hide()')
            exec(f'self.spinBoxKernel{i}.hide()')

    def _SetSpinBoxes(self, spinboxes=dict):
        for key, values in spinboxes.items():
            if key[:len(key) - 1] == 'spinBox':
                number = re.search(r'\d+', key).group(0)
                exec(f'self.label{number}.setText(\'{values["name"]}\')')
                exec(f'self.label{number}.show()')
            exec(f'self.{key}.setMinimum({values["min"]})')
            exec(f'self.{key}.setMaximum({values["max"]})')
            exec(f'self.{key}.setSingleStep({values["step"]})')
            exec(f'self.{key}.setValue({values["value"]})')
            exec(f'self.{key}.show()')

    def _SetAccessKernelSpinBoxes(self):
        if self.comboBoxType.currentText() == "Sharpen":
            for i in range(1, 10):
                exec(f'self.spinBoxKernel{i}.setEnabled(False)')
        elif self.comboBoxType.currentText() == "My Variant":
            for i in range(1, 10):
                exec(f'self.spinBoxKernel{i}.setEnabled(True)')

    def _ApplyMethod(self, category, name, index):
        if category == "Blur":
            self._ApplyBlurMethod(name, index)
        elif category == "Edge Detection":
            self._ApplyEdgeDetectionMethod(name, index)
        elif category == "Morphology":
            self._ApplyMorphologyMethod(name, index)
        elif category == "Kernel":
            self._ApplyKernelMethod(name, index)

    def _ApplyBlurMethod(self, name, index):
        if name == "Average":
            self.image_process.image = \
                self.image_process.blur.Average(image=self.image_process.image,
                                                ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Bilateral":
            self.image_process.image = \
                self.image_process.blur.Bilateral(image=self.image_process.image,
                                                  fsize=self.image_process.temp_images[index]['filter size'],
                                                  sigmaColor=self.image_process.temp_images[index]['sigma color'],
                                                  sigmaSpace=self.image_process.temp_images[index]['sigma space'])
        elif name == "Gaussian":
            self.image_process.image = \
                self.image_process.blur.Gaussian(image=self.image_process.image,
                                                 ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Median":
            self.image_process.image = \
                self.image_process.blur.Median(image=self.image_process.image,
                                               ksize=self.image_process.temp_images[index]['kernel size'])

    def _ApplyEdgeDetectionMethod(self, name, index):
        if name == "Canny":
            self.image_process.image = \
                self.image_process.edge_detection.Canny(image=self.image_process.image,
                                                        thresh1=self.image_process.temp_images[index]['first thresh'],
                                                        thresh2=self.image_process.temp_images[index]['second thresh'])
        elif name == "Laplacian":
            self.image_process.image = self.image_process.edge_detection.Laplacian(image=self.image_process.image)
        elif name == "Sobel":
            self.image_process.image = \
                self.image_process.edge_detection.SobelX(image=self.image_process.image,
                                                         ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Sobel X":
            self.image_process.image = \
                self.image_process.edge_detection.SobelX(image=self.image_process.image,
                                                         ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Sobel Y":
            self.image_process.image = \
                self.image_process.edge_detection.SobelY(image=self.image_process.image,
                                                         ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Scharr X":
            self.image_process.image = self.image_process.edge_detection.ScharrX(image=self.image_process.image)
        elif name == "Scharr Y":
            self.image_process.image = self.image_process.edge_detection.ScharrY(image=self.image_process.image)
        elif name == "Simple Thresholding":
            self.image_process.image = \
                self.image_process.edge_detection.SimpleThresholding(
                    image=self.image_process.image, thresh=self.image_process.temp_images[index]['thresh'])
        elif name == "Adaptive Thresholding":
            self.image_process.image = self.image_process.edge_detection.AdaptiveThresholding(
                image=self.image_process.image,
                area=self.image_process.temp_images[index]['area'],
                const=self.image_process.temp_images[index]['const'])

    def _ApplyMorphologyMethod(self, name, index):
        if name == "Open":
            self.image_process.image = \
                self.image_process.morphology.Open(
                    image=self.image_process.image,
                    ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Close":
            self.image_process.image = \
                self.image_process.morphology.Close(
                    image=self.image_process.image,
                    ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Gradient":
            self.image_process.image = \
                self.image_process.morphology.Gradient(
                    image=self.image_process.image,
                    ksize=self.image_process.temp_images[index]['kernel size'])
        elif name == "Dilate":
            self.image_process.image = \
                self.image_process.morphology.Dilate(
                    image=self.image_process.image,
                    ksize=self.image_process.temp_images[index]['kernel size'],
                    iterations=self.image_process.temp_images[index]['iterations'])
        elif name == "Erode":
            self.image_process.image = \
                self.image_process.morphology.Erode(
                    image=self.image_process.image,
                    ksize=self.image_process.temp_images[index]['kernel size'],
                    iterations=self.image_process.temp_images[index]['iterations'])

    def _ApplyKernelMethod(self, name, index):
        if name == "Sharpen":
            self.image_process.image = \
                self.image_process.kernel.Sharpen(self.image_process.image,
                                                  self.image_process.temp_images[index]['matrix'])
        elif name == "My Variant":
            self.image_process.image = \
                self.image_process.kernel.MyVariant(self.image_process.image,
                                                    self.image_process.temp_images[index]['matrix'])

    # !-!-!-!-!
    def _DefineImageOrientation(self):
        height, width = self.image_process.original_image.shape[:2]
        if height >= width:
            orientation = True  # вертикальная ориентация
        elif height < width:
            orientation = False  # горизонтальная ориентация
        return orientation

    # !-!-!-!-!
    def _ResizeImage(self):  # поменять название на что-то больее подходящее
        height, width = self.image_process.original_image.shape[:2]
        ref_height = 800
        ref_width = 525
        ref_diagonal = math.sqrt(ref_height*ref_height + ref_width*ref_width)
        diagonal = math.sqrt(height*height + width*width)
        if diagonal > ref_diagonal:
            scale_percent = ref_diagonal / diagonal
            return scale_percent
        else:
            scale_percent = 1
            return scale_percent

    # ROBOT EVENTS AND FUNCTIONAL
    def _FindContours(self):
        if len(self.image_process.temp_images) == 0:
            self.image_process.image = cv2.imread('Data/Temp/Original.jpg')
        else:
            self.image_process.image = cv2.imread(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        thresh = self.spinBoxThreshold.value()
        area = self.spinBoxArea.value()
        approx_type = self.comboBoxApprox.currentText()
        if approx_type == "Simple":
            approx_type = cv2.CHAIN_APPROX_SIMPLE
        elif approx_type == "TC89_KCOS":
            approx_type = cv2.CHAIN_APPROX_TC89_KCOS
        elif approx_type == "TC89_L1":
            approx_type = cv2.CHAIN_APPROX_TC89_L1
        contours = FindContours(self.image_process.image, thresh, area, approx_type)[0]
        clean_contours = FindContours(self.image_process.image, thresh, area, approx_type)[1]
        self.image_process.image = FindContours(self.image_process.image, thresh, area, approx_type)[2]
        self.textBoxTotal.setText(str(len(contours)))
        self.textBoxClean.setText(str(len(clean_contours)))
        cv2.imwrite('Data/Temp/Contours.jpg', self.image_process.image)
        self._SetImagePictureBoxOutput2('Data/Temp/Contours.jpg')
        return clean_contours
        # Домножаем координаты на вычисленный scale_percent, вызывая функцию _ResizeImage.
        # Но не так просто здесь, надо подумать, где и когда это лучше сделать (в _Draw?).
        # Или здесь scale_percent = 1,
        # а в _Draw в дополнительном цикле в зависимости от размеров скалировать clean_contours

        # создать доп функцию Scaling, отвечающую за поворот изображения и изменение его размера?

    def _FindInitPosition(self):
        QMessageBox.about(self, "Предупреждение", "Сейчас робот начнет поиск листа. Будьте осторожны.")
        ip = self.textBoxIP.text()
        speed = self.spinBoxSpeed.value()
        x = 0.583   # временная заглушка
        y = -0.161  # временная заглушка
        z = 0.33    # временная заглушка
        FindInitPosition(ip, speed, x, y, z)
        QMessageBox.about(self, " ", "Робот в начальной позиции и готов к рисованию.")
        # Определеяем ориентацию листа и сравниваем с ориентацией изображения (вызов _DefineImageOrientation)
        # Если не совпадают, то

    def _Draw(self):
        QMessageBox.about(self, "Предупреждение", "Сейчас робот начнет рисование. Будьте осторожны.")
        ip = self.textBoxIP.text()
        speed = self.spinBoxSpeed.value()
        x = 0.583   # временная заглушка
        y = -0.161  # временная заглушка
        z = 0.33    # временная заглушка
        clean_contours = self._FindContours()
        Draw(ip, speed, x, y, z, clean_contours)
        QMessageBox.about(self, " ", "Рисование окончено. Можете забрать рисунок.")

    def _Stop(self):
        ip = self.textBoxIP.text()
        Stop(ip)
        QMessageBox.about(self, " ", "Робот остановлен. Чтобы начать рисование, "
                                     "роботу необходимо вернуться в начальную позицию.")

    def _Hatch(self):
        pass
