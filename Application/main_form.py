import cv2
import numpy as np
import json
import re
import io
import contextlib
import os

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
        self.method_parameters = self.__GetConfiguration()

        # Buttons
        self.buttonLoadImage.clicked.connect(self.__ButtonLoadImageClicked)
        self.buttonPhoto.clicked.connect(self.__ButtonPhotoClicked)
        self.buttonSaveImage.clicked.connect(self.__ButtonSaveImageClicked)
        self.buttonApply.clicked.connect(self.__ButtonApplyClicked)
        self.buttonRemove.clicked.connect(self.__ButtonRemoveClicked)
        self.buttonClear.clicked.connect(self.__ButtonClearClicked)
        self.buttonFindInitPosition.clicked.connect(self.__FindInitPosition)
        self.buttonDraw.clicked.connect(self.__Draw)
        self.buttonStop.clicked.connect(self.__Stop)

        # PictureBoxes
        # ListBoxes

        # ComboBoxes
        self.command_list = {'Blur': ["Average", "Bilateral", "Gaussian", "Median"],
                             'Kernel': ["Sharpen", "My Variant"],
                             'Edge Detection': ["Canny", "Laplacian", "Sobel X", "Sobel Y", "Sobel", "Scharr X",
                                                "Scharr Y", "Simple Thresholding", "Adaptive Thresholding"],
                             'Morphology': ["Dilate", "Erode", "Close", "Open", "Gradient"]
                             }
        self.comboBoxCategory.addItems(self.command_list.keys())
        self.__SetComboboxItems(category=self.comboBoxCategory.currentText())
        self.comboBoxCategory.currentTextChanged.connect(self.__ComboboxCategoryChanged)
        self.comboBoxType.currentTextChanged.connect(self.__ComboboxTypeChanged)

        # Labels

        # SpinBoxes
        self.spinBoxThreshold.valueChanged.connect(self.__FindContours)
        self.spinBoxArea.valueChanged.connect(self.__FindContours)
        self.comboBoxType.activated[str].connect(self.__SetAccessKernelSpinBoxes)
        self.__HideAllSpinBoxes()
        self.__SetSpinBoxes(self.method_parameters[self.comboBoxCategory.currentText()]
                            [self.comboBoxType.currentText()])

    # IMAGE PROCESSING EVENTS
    def __ButtonLoadImageClicked(self):
        self.image_path = QFileDialog.getOpenFileName(filter='Изображения (*.jpg *.jpeg *.png)')
        self.image_path = self.image_path[0]
        if len(self.image_path) > 0:
            self.image_process.image = cv2.imread(self.image_path)
            self.image_process.original_image = self.image_process.image
            cv2.imwrite('Data/Temp/Original.jpg', self.image_process.original_image)
            self.__SetImagePictureBoxOriginal('Data/Temp/Original.jpg')
            self.__SetImagePictureBoxOutput('Data/Temp/Original.jpg')
            self.__SetImagePictureBoxOutput2('Data/Temp/Original.jpg')
            self.listBoxImages.clear()
        else:
            return

    def __ButtonPhotoClicked(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret, frame = camera.read()
            cv2.imshow('Press "q" to take a photo', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.listBoxImages.clear()
                self.image_process.image = frame
                self.image_process.original_image = frame
                cv2.imwrite('Data/Temp/Original.jpg', self.image_process.original_image)
                self.__SetImagePictureBoxOriginal('Data/Temp/Original.jpg')
                self.__SetImagePictureBoxOutput('Data/Temp/Original.jpg')
                self.__SetImagePictureBoxOutput2('Data/Temp/Original.jpg')
                break
        camera.release()
        cv2.destroyAllWindows()

    def __ButtonSaveImageClicked(self):
        self.image_process.image = cv2.imread(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self.image_path = QFileDialog.getSaveFileName(filter='JPG (*.jpg);; PNG (*.png)')
        self.image_path = self.image_path[0]
        if len(self.image_path) > 0:
            cv2.imwrite(self.image_path, self.image_process.image)
        else:
            return

    def __ButtonApplyClicked(self):
        category = self.comboBoxCategory.currentText()
        name = self.comboBoxType.currentText()
        text, method = self.__GetMethodInfo(self.comboBoxCategory.currentText(), self.comboBoxType.currentText(),
                                            self.method_parameters[self.comboBoxCategory.currentText()]
                                            [self.comboBoxType.currentText()])
        self.image_process.temp_images.append(method)
        self.__ApplyMethod(category, name, len(self.image_process.temp_images) - 1)
        cv2.imwrite(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg', self.image_process.image)
        self.__SetImagePictureBoxOutput(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self.__SetImagePictureBoxOutput2(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        self.__SetListboxItem(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg', text)

    def __ButtonRemoveClicked(self):
        index = self.listBoxImages.currentRow()
        self.image_process.temp_images.pop(index)
        self.image_process.image = self.image_process.original_image
        self.listBoxImages.takeItem(index)
        for index in range(len(self.image_process.temp_images)):
            self.__ApplyMethod(self.image_process.temp_images[index]['category'],
                               self.image_process.temp_images[index]['name'],
                               index)
            cv2.imwrite(f'Data/Temp/Temp{index}.jpg', self.image_process.image)
        if self.image_process.temp_images:
            self.__SetImagePictureBoxOutput(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
            self.__SetImagePictureBoxOutput2(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        else:
            self.__SetImagePictureBoxOutput(f'Data/Temp/Original.jpg')
            self.__SetImagePictureBoxOutput2(f'Data/Temp/Original.jpg')

    def __ButtonClearClicked(self):
        for i in range(len(self.image_process.temp_images)):
            os.remove(f'Data/Temp/Temp{i}.jpg')
        self.listBoxImages.clear()
        self.__SetImagePictureBoxOutput(f'Data/Temp/Original.jpg')
        self.__SetImagePictureBoxOutput2(f'Data/Temp/Original.jpg')

    def __ComboboxCategoryChanged(self, value):
        self.__SetComboboxItems(category=value)

    def __ComboboxTypeChanged(self, value):
        if self.comboBoxType.count() == 0:
            return
        self.__HideAllSpinBoxes()
        self.__SetSpinBoxes(self.method_parameters[self.comboBoxCategory.currentText()][value])

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
    def __SetComboboxItems(self, category):
        self.comboBoxType.clear()
        self.comboBoxType.addItems(self.command_list[category])

    def __SetListboxItem(self, image_path, text):
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.listBoxImages.iconSize(), Qt.KeepAspectRatio)
        item = QListWidgetItem()
        item.setIcon(QIcon(self.pixmap))
        item.setText(self.comboBoxType.currentText())
        item.setToolTip(text)
        self.listBoxImages.addItem(item)

    def __SetImagePictureBoxOriginal(self, image_path):
        # Picture Box Original
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.pictureBoxOriginal.size(), Qt.KeepAspectRatio)
        self.pictureBoxOriginal.setAlignment(Qt.AlignCenter)
        self.pictureBoxOriginal.setPixmap(self.pixmap)

    def __SetImagePictureBoxOutput(self, image_path):
        # Picture Box Output
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.pictureBoxOutput.size(), Qt.KeepAspectRatio)
        self.pictureBoxOutput.setAlignment(Qt.AlignCenter)
        self.pictureBoxOutput.setPixmap(self.pixmap)
        # Picture Box Processed
        self.pixmap = self.pixmap.scaled(self.pictureBoxProcessed.size(), Qt.KeepAspectRatio)
        self.pictureBoxProcessed.setAlignment(Qt.AlignCenter)
        self.pictureBoxProcessed.setPixmap(self.pixmap)

    def __SetImagePictureBoxOutput2(self, image_path):
        # Picture Box Output 2
        self.pixmap = QPixmap(QImage(image_path))
        self.pixmap = self.pixmap.scaled(self.pictureBoxOutput2.size(), Qt.KeepAspectRatio)
        self.pictureBoxOutput2.setAlignment(Qt.AlignCenter)
        self.pictureBoxOutput2.setPixmap(self.pixmap)

    def __GetMethodInfo(self, category, name, parameters=dict):
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
            text.append(f"matrix:\n {self.__GetKernel()}")
            method['matrix'] = self.__GetKernel()
        text = "; ".join(text)
        return text, method

    def __GetConfiguration(self):
        with open('Data/Parameters.json') as file:
            data = json.load(file)
        return data

    def __GetKernel(self):
        return np.array([[self.spinBoxKernel1.value(), self.spinBoxKernel2.value(), self.spinBoxKernel3.value()],
                         [self.spinBoxKernel4.value(), self.spinBoxKernel5.value(), self.spinBoxKernel6.value()],
                         [self.spinBoxKernel7.value(), self.spinBoxKernel8.value(), self.spinBoxKernel9.value()]])

    def __HideAllSpinBoxes(self):
        for i in range(1, 10):
            if i < 6:
                exec(f'self.label{i}.hide()')
                exec(f'self.spinBox{i}.hide()')
            exec(f'self.spinBoxKernel{i}.hide()')

    def __SetSpinBoxes(self, spinboxes=dict):
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

    def __SetAccessKernelSpinBoxes(self):
        if self.comboBoxType.currentText() == "Sharpen":
            for i in range(1, 10):
                exec(f'self.spinBoxKernel{i}.setEnabled(False)')
        elif self.comboBoxType.currentText() == "My Variant":
            for i in range(1, 10):
                exec(f'self.spinBoxKernel{i}.setEnabled(True)')

    def __ApplyMethod(self, category, name, index):
        if category == "Blur":
            self.__ApplyBlurMethod(name, index)
        elif category == "Edge Detection":
            self.__ApplyEdgeDetectionMethod(name, index)
        elif category == "Morphology":
            self.__ApplyMorphologyMethod(name, index)
        elif category == "Kernel":
            self.__ApplyKernelMethod(name, index)

    def __ApplyBlurMethod(self, name, index):
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

    def __ApplyEdgeDetectionMethod(self, name, index):
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

    def __ApplyMorphologyMethod(self, name, index):
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

    def __ApplyKernelMethod(self, name, index):
        if name == "Sharpen":
            self.image_process.image = \
                self.image_process.kernel.Sharpen(self.image_process.image,
                                                  self.image_process.temp_images[index]['matrix'])
        elif name == "My Variant":
            self.image_process.image = \
                self.image_process.kernel.MyVariant(self.image_process.image,
                                                    self.image_process.temp_images[index]['matrix'])

    # ROBOT EVENTS AND FUNCTIONAL
    def __FindContours(self):
        if len(self.image_process.temp_images) == 0:
            self.image_process.image = cv2.imread('Data/Temp/Original.jpg')
        else:
            self.image_process.image = cv2.imread(f'Data/Temp/Temp{len(self.image_process.temp_images) - 1}.jpg')
        thresh = self.spinBoxThreshold.value()
        area = self.spinBoxArea.value()
        contours = FindContours(self.image_process.image, thresh, area)[0]
        clean_contours = FindContours(self.image_process.image, thresh, area)[1]
        self.image_process.image = FindContours(self.image_process.image, thresh, area)[2]
        self.textBoxTotal.setText(str(len(contours)))
        self.textBoxClean.setText(str(len(clean_contours)))
        cv2.imwrite('Data/Temp/Contours.jpg', self.image_process.image)
        self.__SetImagePictureBoxOutput2('Data/Temp/Contours.jpg')
        return clean_contours

    def __FindInitPosition(self):
        QMessageBox.about(self, "Предупреждение", "Сейчас робот начнет поиск листа. "
                                                  "Будьте осторожны.")
        ip = self.textBoxIP.text()
        speed = self.spinBoxSpeed.value()
        x = 0.583   # временная заглушка
        y = -0.161  # временная заглушка
        z = 0.33    # временная заглушка
        FindInitPosition(ip, speed, x, y, z)
        QMessageBox.about(self, " ", "Робот в начальной позиции и готов к рисованию.")

    def __Draw(self):
        QMessageBox.about(self, "Предупреждение", "Сейчас робот начнет рисование. Будьте осторожны.")
        ip = self.textBoxIP.text()
        speed = self.spinBoxSpeed.value()
        x = 0.583   # временная заглушка
        y = -0.161  # временная заглушка
        z = 0.33    # временная заглушка
        clean_contours = self.__FindContours()
        Draw(ip, speed, x, y, z, clean_contours)
        QMessageBox.about(self, " ", "Рисование окончено. Можете забрать рисунок.")

    def __Stop(self):
        ip = self.textBoxIP.text()
        Stop(ip)
        QMessageBox.about(self, " ", "Робот остановлен. Чтобы начать рисование, "
                                     "роботу необходимо вернуться в начальную позицию.")

    def __Hatch(self):
        pass
