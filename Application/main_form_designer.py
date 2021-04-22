from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tabImageProcessing = QtWidgets.QWidget()
        self.tabImageProcessing.setStyleSheet("")
        self.tabImageProcessing.setObjectName("tabImageProcessing")
        self.pictureBoxOutput = QtWidgets.QLabel(self.tabImageProcessing)
        self.pictureBoxOutput.setGeometry(QtCore.QRect(20, 40, 900, 630))
        self.pictureBoxOutput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOutput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOutput.setLineWidth(1)
        self.pictureBoxOutput.setText("")
        self.pictureBoxOutput.setScaledContents(False)
        self.pictureBoxOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pictureBoxOutput.setWordWrap(False)
        self.pictureBoxOutput.setObjectName("pictureBoxOutput")
        self.groupBoxOriginal = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxOriginal.setGeometry(QtCore.QRect(940, 0, 320, 200))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxOriginal.setFont(font)
        self.groupBoxOriginal.setObjectName("groupBoxOriginal")
        self.pictureBoxOriginal = QtWidgets.QLabel(self.groupBoxOriginal)
        self.pictureBoxOriginal.setGeometry(QtCore.QRect(14, 20, 291, 171))
        self.pictureBoxOriginal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOriginal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOriginal.setLineWidth(1)
        self.pictureBoxOriginal.setText("")
        self.pictureBoxOriginal.setScaledContents(False)
        self.pictureBoxOriginal.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureBoxOriginal.setWordWrap(False)
        self.pictureBoxOriginal.setObjectName("pictureBoxOriginal")
        self.groupBoxHistory = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxHistory.setGeometry(QtCore.QRect(940, 200, 320, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxHistory.setFont(font)
        self.groupBoxHistory.setStyleSheet("")
        self.groupBoxHistory.setFlat(False)
        self.groupBoxHistory.setObjectName("groupBoxHistory")
        self.listBoxImages = QtWidgets.QListWidget(self.groupBoxHistory)
        self.listBoxImages.setGeometry(QtCore.QRect(10, 20, 300, 120))
        self.listBoxImages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listBoxImages.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listBoxImages.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listBoxImages.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listBoxImages.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listBoxImages.setIconSize(QtCore.QSize(90, 63))
        self.listBoxImages.setViewMode(QtWidgets.QListView.ListMode)
        self.listBoxImages.setObjectName("listBoxImages")
        self.buttonRemove = QtWidgets.QPushButton(self.groupBoxHistory)
        self.buttonRemove.setEnabled(True)
        self.buttonRemove.setGeometry(QtCore.QRect(30, 145, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonRemove.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonRemove.setAutoDefault(False)
        self.buttonRemove.setDefault(False)
        self.buttonRemove.setFlat(False)
        self.buttonRemove.setObjectName("buttonRemove")
        self.buttonClear = QtWidgets.QPushButton(self.groupBoxHistory)
        self.buttonClear.setEnabled(True)
        self.buttonClear.setGeometry(QtCore.QRect(170, 145, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonClear.setFont(font)
        self.buttonClear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonClear.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonClear.setAutoDefault(False)
        self.buttonClear.setDefault(False)
        self.buttonClear.setFlat(False)
        self.buttonClear.setObjectName("buttonClear")
        self.groupBoxCommands = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxCommands.setGeometry(QtCore.QRect(940, 380, 320, 271))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxCommands.setFont(font)
        self.groupBoxCommands.setObjectName("groupBoxCommands")
        self.comboBoxCategory = QtWidgets.QComboBox(self.groupBoxCommands)
        self.comboBoxCategory.setGeometry(QtCore.QRect(10, 20, 300, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setStyleSheet("QComboBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color:white;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Work/Diploma Project/Application/Alternative Cobot/Resource/arrow1.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.comboBoxType = QtWidgets.QComboBox(self.groupBoxCommands)
        self.comboBoxType.setGeometry(QtCore.QRect(10, 50, 300, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        self.comboBoxType.setFont(font)
        self.comboBoxType.setStyleSheet("QComboBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color:white;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Work/Diploma Project/Application/Alternative Cobot/Resource/arrow1.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBoxType.setObjectName("comboBoxType")
        self.spinBoxKernel1 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel1.setEnabled(False)
        self.spinBoxKernel1.setGeometry(QtCore.QRect(90, 80, 42, 22))
        self.spinBoxKernel1.setObjectName("spinBoxKernel1")
        self.spinBoxKernel2 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel2.setEnabled(False)
        self.spinBoxKernel2.setGeometry(QtCore.QRect(140, 80, 42, 22))
        self.spinBoxKernel2.setObjectName("spinBoxKernel2")
        self.spinBoxKernel3 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel3.setEnabled(False)
        self.spinBoxKernel3.setGeometry(QtCore.QRect(190, 80, 42, 22))
        self.spinBoxKernel3.setObjectName("spinBoxKernel3")
        self.spinBoxKernel4 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel4.setEnabled(False)
        self.spinBoxKernel4.setGeometry(QtCore.QRect(90, 110, 42, 22))
        self.spinBoxKernel4.setObjectName("spinBoxKernel4")
        self.spinBoxKernel5 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel5.setEnabled(False)
        self.spinBoxKernel5.setGeometry(QtCore.QRect(140, 110, 42, 22))
        self.spinBoxKernel5.setObjectName("spinBoxKernel5")
        self.spinBoxKernel6 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel6.setEnabled(False)
        self.spinBoxKernel6.setGeometry(QtCore.QRect(190, 110, 42, 22))
        self.spinBoxKernel6.setObjectName("spinBoxKernel6")
        self.spinBoxKernel7 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel7.setEnabled(False)
        self.spinBoxKernel7.setGeometry(QtCore.QRect(90, 140, 42, 22))
        self.spinBoxKernel7.setObjectName("spinBoxKernel7")
        self.spinBoxKernel8 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel8.setEnabled(False)
        self.spinBoxKernel8.setGeometry(QtCore.QRect(140, 140, 42, 22))
        self.spinBoxKernel8.setObjectName("spinBoxKernel8")
        self.spinBoxKernel9 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBoxKernel9.setEnabled(False)
        self.spinBoxKernel9.setGeometry(QtCore.QRect(190, 140, 42, 22))
        self.spinBoxKernel9.setObjectName("spinBoxKernel9")
        self.spinBox1 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBox1.setGeometry(QtCore.QRect(10, 80, 61, 22))
        self.spinBox1.setObjectName("spinBox1")
        self.spinBox2 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBox2.setGeometry(QtCore.QRect(10, 110, 61, 22))
        self.spinBox2.setObjectName("spinBox2")
        self.spinBox3 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBox3.setGeometry(QtCore.QRect(10, 140, 61, 22))
        self.spinBox3.setObjectName("spinBox3")
        self.spinBox4 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBox4.setGeometry(QtCore.QRect(10, 170, 61, 22))
        self.spinBox4.setObjectName("spinBox4")
        self.spinBox5 = QtWidgets.QSpinBox(self.groupBoxCommands)
        self.spinBox5.setGeometry(QtCore.QRect(10, 200, 61, 22))
        self.spinBox5.setObjectName("spinBox5")
        self.buttonApply = QtWidgets.QPushButton(self.groupBoxCommands)
        self.buttonApply.setEnabled(True)
        self.buttonApply.setGeometry(QtCore.QRect(100, 230, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonApply.setFont(font)
        self.buttonApply.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonApply.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonApply.setAutoDefault(False)
        self.buttonApply.setDefault(False)
        self.buttonApply.setFlat(False)
        self.buttonApply.setObjectName("buttonApply")
        self.label1 = QtWidgets.QLabel(self.groupBoxCommands)
        self.label1.setGeometry(QtCore.QRect(80, 80, 171, 16))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.groupBoxCommands)
        self.label2.setGeometry(QtCore.QRect(80, 110, 171, 16))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.groupBoxCommands)
        self.label3.setGeometry(QtCore.QRect(80, 140, 171, 16))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.groupBoxCommands)
        self.label4.setGeometry(QtCore.QRect(80, 170, 171, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.groupBoxCommands)
        self.label5.setGeometry(QtCore.QRect(80, 200, 171, 16))
        self.label5.setObjectName("label5")
        self.buttonLoadImage = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonLoadImage.setEnabled(True)
        self.buttonLoadImage.setGeometry(QtCore.QRect(10, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonLoadImage.setFont(font)
        self.buttonLoadImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonLoadImage.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonLoadImage.setAutoDefault(False)
        self.buttonLoadImage.setDefault(False)
        self.buttonLoadImage.setFlat(False)
        self.buttonLoadImage.setObjectName("buttonLoadImage")
        self.buttonPhoto = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonPhoto.setEnabled(True)
        self.buttonPhoto.setGeometry(QtCore.QRect(140, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonPhoto.setFont(font)
        self.buttonPhoto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonPhoto.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonPhoto.setAutoDefault(False)
        self.buttonPhoto.setDefault(False)
        self.buttonPhoto.setFlat(False)
        self.buttonPhoto.setObjectName("buttonPhoto")
        self.buttonSaveImage = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonSaveImage.setEnabled(True)
        self.buttonSaveImage.setGeometry(QtCore.QRect(270, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonSaveImage.setFont(font)
        self.buttonSaveImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSaveImage.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonSaveImage.setAutoDefault(False)
        self.buttonSaveImage.setDefault(False)
        self.buttonSaveImage.setFlat(False)
        self.buttonSaveImage.setObjectName("buttonSaveImage")
        self.tabWidget.addTab(self.tabImageProcessing, "")
        self.tabRobotInteraction = QtWidgets.QWidget()
        self.tabRobotInteraction.setObjectName("tabRobotInteraction")
        self.pictureBoxOutput2 = QtWidgets.QLabel(self.tabRobotInteraction)
        self.pictureBoxOutput2.setGeometry(QtCore.QRect(20, 40, 900, 630))
        self.pictureBoxOutput2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOutput2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOutput2.setLineWidth(1)
        self.pictureBoxOutput2.setText("")
        self.pictureBoxOutput2.setScaledContents(False)
        self.pictureBoxOutput2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pictureBoxOutput2.setWordWrap(False)
        self.pictureBoxOutput2.setObjectName("pictureBoxOutput2")
        self.groupBoxContours = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxContours.setGeometry(QtCore.QRect(940, 200, 320, 201))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxContours.setFont(font)
        self.groupBoxContours.setObjectName("groupBoxContours")
        self.spinBoxThreshold = QtWidgets.QSpinBox(self.groupBoxContours)
        self.spinBoxThreshold.setEnabled(True)
        self.spinBoxThreshold.setGeometry(QtCore.QRect(10, 20, 61, 22))
        self.spinBoxThreshold.setMaximum(500)
        self.spinBoxThreshold.setObjectName("spinBoxThreshold")
        self.labelContours1 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours1.setGeometry(QtCore.QRect(80, 20, 231, 16))
        self.labelContours1.setObjectName("labelContours1")
        self.textBoxTotal = QtWidgets.QLineEdit(self.groupBoxContours)
        self.textBoxTotal.setEnabled(False)
        self.textBoxTotal.setGeometry(QtCore.QRect(10, 110, 61, 22))
        self.textBoxTotal.setObjectName("textBoxTotal")
        self.textBoxClean = QtWidgets.QLineEdit(self.groupBoxContours)
        self.textBoxClean.setEnabled(False)
        self.textBoxClean.setGeometry(QtCore.QRect(10, 140, 61, 22))
        self.textBoxClean.setObjectName("textBoxClean")
        self.labelContours3 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours3.setGeometry(QtCore.QRect(80, 110, 231, 16))
        self.labelContours3.setObjectName("labelContours3")
        self.labelContours4 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours4.setGeometry(QtCore.QRect(80, 140, 231, 16))
        self.labelContours4.setObjectName("labelContours4")
        self.spinBoxArea = QtWidgets.QSpinBox(self.groupBoxContours)
        self.spinBoxArea.setEnabled(True)
        self.spinBoxArea.setGeometry(QtCore.QRect(10, 50, 61, 22))
        self.spinBoxArea.setMaximum(500)
        self.spinBoxArea.setObjectName("spinBoxArea")
        self.labelContours2 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours2.setGeometry(QtCore.QRect(80, 50, 231, 16))
        self.labelContours2.setObjectName("labelContours2")
        self.checkBox_hatching = QtWidgets.QCheckBox(self.groupBoxContours)
        self.checkBox_hatching.setGeometry(QtCore.QRect(10, 170, 301, 20))
        self.checkBox_hatching.setObjectName("checkBox_hatching")
        self.comboBoxApprox = QtWidgets.QComboBox(self.groupBoxContours)
        self.comboBoxApprox.setGeometry(QtCore.QRect(10, 80, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        self.comboBoxApprox.setFont(font)
        self.comboBoxApprox.setStyleSheet("QComboBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color:white;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(D:/Work/Diploma Project/Application/Alternative Cobot/Resource/arrow1.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBoxApprox.setObjectName("comboBoxApprox")
        self.labelContours3_2 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours3_2.setGeometry(QtCore.QRect(170, 80, 141, 16))
        self.labelContours3_2.setObjectName("labelContours3_2")
        self.groupBoxProcessed = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxProcessed.setGeometry(QtCore.QRect(940, 0, 320, 200))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxProcessed.setFont(font)
        self.groupBoxProcessed.setObjectName("groupBoxProcessed")
        self.pictureBoxProcessed = QtWidgets.QLabel(self.groupBoxProcessed)
        self.pictureBoxProcessed.setGeometry(QtCore.QRect(14, 20, 291, 171))
        self.pictureBoxProcessed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxProcessed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxProcessed.setLineWidth(1)
        self.pictureBoxProcessed.setText("")
        self.pictureBoxProcessed.setScaledContents(False)
        self.pictureBoxProcessed.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureBoxProcessed.setWordWrap(False)
        self.pictureBoxProcessed.setObjectName("pictureBoxProcessed")
        self.groupBoxRobot = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxRobot.setGeometry(QtCore.QRect(940, 400, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxRobot.setFont(font)
        self.groupBoxRobot.setObjectName("groupBoxRobot")
        self.textBoxIP = QtWidgets.QLineEdit(self.groupBoxRobot)
        self.textBoxIP.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.textBoxIP.setObjectName("textBoxIP")
        self.labelRobot1 = QtWidgets.QLabel(self.groupBoxRobot)
        self.labelRobot1.setGeometry(QtCore.QRect(170, 20, 121, 16))
        self.labelRobot1.setObjectName("labelRobot1")
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.groupBoxRobot)
        self.spinBoxSpeed.setEnabled(True)
        self.spinBoxSpeed.setGeometry(QtCore.QRect(10, 50, 61, 22))
        self.spinBoxSpeed.setMinimum(1)
        self.spinBoxSpeed.setMaximum(100)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.labelRobot2 = QtWidgets.QLabel(self.groupBoxRobot)
        self.labelRobot2.setGeometry(QtCore.QRect(80, 50, 191, 16))
        self.labelRobot2.setObjectName("labelRobot2")
        self.buttonFindInitPosition = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonFindInitPosition.setEnabled(True)
        self.buttonFindInitPosition.setGeometry(QtCore.QRect(1040, 490, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonFindInitPosition.setFont(font)
        self.buttonFindInitPosition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonFindInitPosition.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonFindInitPosition.setAutoDefault(False)
        self.buttonFindInitPosition.setDefault(False)
        self.buttonFindInitPosition.setFlat(False)
        self.buttonFindInitPosition.setObjectName("buttonFindInitPosition")
        self.buttonDraw = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonDraw.setEnabled(True)
        self.buttonDraw.setGeometry(QtCore.QRect(1040, 530, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonDraw.setFont(font)
        self.buttonDraw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonDraw.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonDraw.setAutoDefault(False)
        self.buttonDraw.setDefault(False)
        self.buttonDraw.setFlat(False)
        self.buttonDraw.setObjectName("buttonDraw")
        self.buttonStop = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonStop.setEnabled(True)
        self.buttonStop.setGeometry(QtCore.QRect(1040, 570, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.buttonStop.setFont(font)
        self.buttonStop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonStop.setStyleSheet("color: black;\n"
"selection-background-color: rgb(227, 227, 227);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"")
        self.buttonStop.setAutoDefault(False)
        self.buttonStop.setDefault(False)
        self.buttonStop.setFlat(False)
        self.buttonStop.setObjectName("buttonStop")
        self.tabWidget.addTab(self.tabRobotInteraction, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CobArt"))
        self.groupBoxOriginal.setTitle(_translate("MainWindow", "Original Image"))
        self.groupBoxHistory.setTitle(_translate("MainWindow", "History"))
        self.buttonRemove.setText(_translate("MainWindow", "Remove"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.groupBoxCommands.setTitle(_translate("MainWindow", "Commands"))
        self.buttonApply.setText(_translate("MainWindow", "Apply"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.label3.setText(_translate("MainWindow", "TextLabel"))
        self.label4.setText(_translate("MainWindow", "TextLabel"))
        self.label5.setText(_translate("MainWindow", "TextLabel"))
        self.buttonLoadImage.setText(_translate("MainWindow", "Load Image"))
        self.buttonPhoto.setText(_translate("MainWindow", "Photo"))
        self.buttonSaveImage.setText(_translate("MainWindow", "Save Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImageProcessing), _translate("MainWindow", "Image Processing"))
        self.groupBoxContours.setTitle(_translate("MainWindow", "Contours detection"))
        self.labelContours1.setText(_translate("MainWindow", "Threshold"))
        self.labelContours3.setText(_translate("MainWindow", "Total number of contours "))
        self.labelContours4.setText(_translate("MainWindow", "Number of \"clean\" contours "))
        self.labelContours2.setText(_translate("MainWindow", "Screening area"))
        self.checkBox_hatching.setText(_translate("MainWindow", "Hatch"))
        self.labelContours3_2.setText(_translate("MainWindow", "Approximation type"))
        self.groupBoxProcessed.setTitle(_translate("MainWindow", "Processed Image"))
        self.groupBoxRobot.setTitle(_translate("MainWindow", "Robot parameters"))
        self.textBoxIP.setText(_translate("MainWindow", "10.10.10.20:8081"))
        self.labelRobot1.setText(_translate("MainWindow", "IP-adress"))
        self.labelRobot2.setText(_translate("MainWindow", "Speed"))
        self.buttonFindInitPosition.setText(_translate("MainWindow", "Find Init Position"))
        self.buttonDraw.setText(_translate("MainWindow", "Draw"))
        self.buttonStop.setText(_translate("MainWindow", "STOP!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRobotInteraction), _translate("MainWindow", "Robot Interaction"))
