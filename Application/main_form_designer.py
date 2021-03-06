from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/Data/Resource/Stylesheets/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/Data/Resource/Stylesheets/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/Data/Resource/Stylesheets/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/Data/Resource/Stylesheets/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/Data/Resource/Stylesheets/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/Data/Resource/Stylesheets/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/Data/Resource/Stylesheets/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/Data/Resource/Stylesheets/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/Data/Resource/Stylesheets/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon    : url(:/Data/Resource/Stylesheets/dark_blue/img/critical.png);\n"
"    messagebox-information-icon    : url(:/Data/Resource/Stylesheets/dark_blue/img/information.png);\n"
"    messagebox-question-icon    : url(:/Data/Resource/Stylesheets/dark_blue/img/question.png);\n"
"    messagebox-warning-icon:    : url(:/Data/Resource/Stylesheets/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabImageProcessing = QtWidgets.QWidget()
        self.tabImageProcessing.setStyleSheet("")
        self.tabImageProcessing.setObjectName("tabImageProcessing")
        self.pictureBoxOutput = QtWidgets.QLabel(self.tabImageProcessing)
        self.pictureBoxOutput.setGeometry(QtCore.QRect(20, 40, 990, 675))
        self.pictureBoxOutput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOutput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOutput.setLineWidth(1)
        self.pictureBoxOutput.setText("")
        self.pictureBoxOutput.setPixmap(QtGui.QPixmap("Data/Resource/ImageArea.png"))
        self.pictureBoxOutput.setScaledContents(False)
        self.pictureBoxOutput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pictureBoxOutput.setWordWrap(False)
        self.pictureBoxOutput.setObjectName("pictureBoxOutput")
        self.groupBoxOriginal = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxOriginal.setGeometry(QtCore.QRect(1025, 0, 320, 230))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxOriginal.setFont(font)
        self.groupBoxOriginal.setObjectName("groupBoxOriginal")
        self.pictureBoxOriginal = QtWidgets.QLabel(self.groupBoxOriginal)
        self.pictureBoxOriginal.setGeometry(QtCore.QRect(14, 30, 291, 191))
        self.pictureBoxOriginal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOriginal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOriginal.setLineWidth(1)
        self.pictureBoxOriginal.setText("")
        self.pictureBoxOriginal.setPixmap(QtGui.QPixmap("Data/Resource/OriginalImage.png"))
        self.pictureBoxOriginal.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureBoxOriginal.setWordWrap(False)
        self.pictureBoxOriginal.setObjectName("pictureBoxOriginal")
        self.groupBoxHistory = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxHistory.setGeometry(QtCore.QRect(1025, 230, 320, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxHistory.setFont(font)
        self.groupBoxHistory.setStyleSheet("")
        self.groupBoxHistory.setFlat(False)
        self.groupBoxHistory.setObjectName("groupBoxHistory")
        self.listBoxImages = QtWidgets.QListWidget(self.groupBoxHistory)
        self.listBoxImages.setGeometry(QtCore.QRect(10, 30, 295, 140))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listBoxImages.setFont(font)
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
        self.buttonRemove.setGeometry(QtCore.QRect(30, 175, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonRemove.setStyleSheet("")
        self.buttonRemove.setAutoDefault(False)
        self.buttonRemove.setDefault(False)
        self.buttonRemove.setFlat(False)
        self.buttonRemove.setObjectName("buttonRemove")
        self.buttonClear = QtWidgets.QPushButton(self.groupBoxHistory)
        self.buttonClear.setEnabled(True)
        self.buttonClear.setGeometry(QtCore.QRect(170, 175, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonClear.setFont(font)
        self.buttonClear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonClear.setStyleSheet("")
        self.buttonClear.setAutoDefault(False)
        self.buttonClear.setDefault(False)
        self.buttonClear.setFlat(False)
        self.buttonClear.setObjectName("buttonClear")
        self.groupBoxOperations = QtWidgets.QGroupBox(self.tabImageProcessing)
        self.groupBoxOperations.setGeometry(QtCore.QRect(1025, 440, 320, 275))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxOperations.setFont(font)
        self.groupBoxOperations.setStyleSheet("")
        self.groupBoxOperations.setObjectName("groupBoxOperations")
        self.comboBoxCategory = QtWidgets.QComboBox(self.groupBoxOperations)
        self.comboBoxCategory.setGeometry(QtCore.QRect(10, 30, 300, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxCategory.setFont(font)
        self.comboBoxCategory.setStyleSheet("")
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.comboBoxType = QtWidgets.QComboBox(self.groupBoxOperations)
        self.comboBoxType.setGeometry(QtCore.QRect(10, 60, 300, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxType.setFont(font)
        self.comboBoxType.setStyleSheet("")
        self.comboBoxType.setObjectName("comboBoxType")
        self.spinBoxKernel1 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel1.setEnabled(False)
        self.spinBoxKernel1.setGeometry(QtCore.QRect(30, 90, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel1.setFont(font)
        self.spinBoxKernel1.setObjectName("spinBoxKernel1")
        self.spinBoxKernel2 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel2.setEnabled(False)
        self.spinBoxKernel2.setGeometry(QtCore.QRect(120, 90, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel2.setFont(font)
        self.spinBoxKernel2.setObjectName("spinBoxKernel2")
        self.spinBoxKernel3 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel3.setEnabled(False)
        self.spinBoxKernel3.setGeometry(QtCore.QRect(210, 90, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel3.setFont(font)
        self.spinBoxKernel3.setObjectName("spinBoxKernel3")
        self.spinBoxKernel4 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel4.setEnabled(False)
        self.spinBoxKernel4.setGeometry(QtCore.QRect(30, 120, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel4.setFont(font)
        self.spinBoxKernel4.setObjectName("spinBoxKernel4")
        self.spinBoxKernel5 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel5.setEnabled(False)
        self.spinBoxKernel5.setGeometry(QtCore.QRect(120, 120, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel5.setFont(font)
        self.spinBoxKernel5.setObjectName("spinBoxKernel5")
        self.spinBoxKernel6 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel6.setEnabled(False)
        self.spinBoxKernel6.setGeometry(QtCore.QRect(210, 120, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel6.setFont(font)
        self.spinBoxKernel6.setObjectName("spinBoxKernel6")
        self.spinBoxKernel7 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel7.setEnabled(False)
        self.spinBoxKernel7.setGeometry(QtCore.QRect(30, 150, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel7.setFont(font)
        self.spinBoxKernel7.setObjectName("spinBoxKernel7")
        self.spinBoxKernel8 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel8.setEnabled(False)
        self.spinBoxKernel8.setGeometry(QtCore.QRect(120, 150, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel8.setFont(font)
        self.spinBoxKernel8.setObjectName("spinBoxKernel8")
        self.spinBoxKernel9 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBoxKernel9.setEnabled(False)
        self.spinBoxKernel9.setGeometry(QtCore.QRect(210, 150, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxKernel9.setFont(font)
        self.spinBoxKernel9.setObjectName("spinBoxKernel9")
        self.spinBox1 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBox1.setGeometry(QtCore.QRect(10, 90, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox1.setFont(font)
        self.spinBox1.setObjectName("spinBox1")
        self.spinBox2 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBox2.setGeometry(QtCore.QRect(10, 120, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox2.setFont(font)
        self.spinBox2.setObjectName("spinBox2")
        self.spinBox3 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBox3.setGeometry(QtCore.QRect(10, 150, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox3.setFont(font)
        self.spinBox3.setObjectName("spinBox3")
        self.spinBox4 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBox4.setGeometry(QtCore.QRect(10, 180, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox4.setFont(font)
        self.spinBox4.setObjectName("spinBox4")
        self.spinBox5 = QtWidgets.QSpinBox(self.groupBoxOperations)
        self.spinBox5.setGeometry(QtCore.QRect(10, 210, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox5.setFont(font)
        self.spinBox5.setObjectName("spinBox5")
        self.buttonApply = QtWidgets.QPushButton(self.groupBoxOperations)
        self.buttonApply.setEnabled(True)
        self.buttonApply.setGeometry(QtCore.QRect(100, 240, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonApply.setFont(font)
        self.buttonApply.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonApply.setStyleSheet("")
        self.buttonApply.setAutoDefault(False)
        self.buttonApply.setDefault(False)
        self.buttonApply.setFlat(False)
        self.buttonApply.setObjectName("buttonApply")
        self.label1 = QtWidgets.QLabel(self.groupBoxOperations)
        self.label1.setEnabled(True)
        self.label1.setGeometry(QtCore.QRect(90, 90, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.groupBoxOperations)
        self.label2.setGeometry(QtCore.QRect(90, 120, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.groupBoxOperations)
        self.label3.setGeometry(QtCore.QRect(90, 150, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.groupBoxOperations)
        self.label4.setGeometry(QtCore.QRect(90, 180, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.groupBoxOperations)
        self.label5.setGeometry(QtCore.QRect(90, 210, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.buttonLoadImage = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonLoadImage.setEnabled(True)
        self.buttonLoadImage.setGeometry(QtCore.QRect(10, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoadImage.setFont(font)
        self.buttonLoadImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonLoadImage.setAutoDefault(False)
        self.buttonLoadImage.setDefault(False)
        self.buttonLoadImage.setFlat(False)
        self.buttonLoadImage.setObjectName("buttonLoadImage")
        self.buttonTakePhoto = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonTakePhoto.setEnabled(True)
        self.buttonTakePhoto.setGeometry(QtCore.QRect(140, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonTakePhoto.setFont(font)
        self.buttonTakePhoto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonTakePhoto.setAutoDefault(False)
        self.buttonTakePhoto.setDefault(False)
        self.buttonTakePhoto.setFlat(False)
        self.buttonTakePhoto.setObjectName("buttonTakePhoto")
        self.buttonSaveImage = QtWidgets.QPushButton(self.tabImageProcessing)
        self.buttonSaveImage.setEnabled(True)
        self.buttonSaveImage.setGeometry(QtCore.QRect(270, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSaveImage.setFont(font)
        self.buttonSaveImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSaveImage.setStyleSheet("")
        self.buttonSaveImage.setAutoDefault(False)
        self.buttonSaveImage.setDefault(False)
        self.buttonSaveImage.setFlat(False)
        self.buttonSaveImage.setObjectName("buttonSaveImage")
        self.tabWidget.addTab(self.tabImageProcessing, "")
        self.tabRobotInteraction = QtWidgets.QWidget()
        self.tabRobotInteraction.setObjectName("tabRobotInteraction")
        self.pictureBoxOutput2 = QtWidgets.QLabel(self.tabRobotInteraction)
        self.pictureBoxOutput2.setGeometry(QtCore.QRect(20, 40, 990, 675))
        self.pictureBoxOutput2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxOutput2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxOutput2.setLineWidth(1)
        self.pictureBoxOutput2.setText("")
        self.pictureBoxOutput2.setScaledContents(False)
        self.pictureBoxOutput2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pictureBoxOutput2.setWordWrap(False)
        self.pictureBoxOutput2.setObjectName("pictureBoxOutput2")
        self.groupBoxContours = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxContours.setGeometry(QtCore.QRect(1025, 230, 320, 181))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxContours.setFont(font)
        self.groupBoxContours.setStyleSheet("")
        self.groupBoxContours.setObjectName("groupBoxContours")
        self.spinBoxThreshold = QtWidgets.QSpinBox(self.groupBoxContours)
        self.spinBoxThreshold.setEnabled(True)
        self.spinBoxThreshold.setGeometry(QtCore.QRect(10, 30, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxThreshold.setFont(font)
        self.spinBoxThreshold.setMaximum(500)
        self.spinBoxThreshold.setObjectName("spinBoxThreshold")
        self.labelContours1 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours1.setGeometry(QtCore.QRect(90, 30, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelContours1.setFont(font)
        self.labelContours1.setStyleSheet("")
        self.labelContours1.setObjectName("labelContours1")
        self.textBoxTotal = QtWidgets.QLineEdit(self.groupBoxContours)
        self.textBoxTotal.setEnabled(False)
        self.textBoxTotal.setGeometry(QtCore.QRect(10, 120, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textBoxTotal.setFont(font)
        self.textBoxTotal.setObjectName("textBoxTotal")
        self.textBoxClean = QtWidgets.QLineEdit(self.groupBoxContours)
        self.textBoxClean.setEnabled(False)
        self.textBoxClean.setGeometry(QtCore.QRect(10, 150, 61, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textBoxClean.setFont(font)
        self.textBoxClean.setObjectName("textBoxClean")
        self.labelContours3 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours3.setGeometry(QtCore.QRect(75, 120, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelContours3.setFont(font)
        self.labelContours3.setObjectName("labelContours3")
        self.labelContours4 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours4.setGeometry(QtCore.QRect(75, 150, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelContours4.setFont(font)
        self.labelContours4.setObjectName("labelContours4")
        self.spinBoxArea = QtWidgets.QSpinBox(self.groupBoxContours)
        self.spinBoxArea.setEnabled(True)
        self.spinBoxArea.setGeometry(QtCore.QRect(10, 60, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxArea.setFont(font)
        self.spinBoxArea.setMaximum(500)
        self.spinBoxArea.setObjectName("spinBoxArea")
        self.labelContours2 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours2.setGeometry(QtCore.QRect(90, 60, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelContours2.setFont(font)
        self.labelContours2.setObjectName("labelContours2")
        self.comboBoxApprox = QtWidgets.QComboBox(self.groupBoxContours)
        self.comboBoxApprox.setGeometry(QtCore.QRect(10, 90, 151, 26))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxApprox.setFont(font)
        self.comboBoxApprox.setStyleSheet("")
        self.comboBoxApprox.setObjectName("comboBoxApprox")
        self.labelContours5 = QtWidgets.QLabel(self.groupBoxContours)
        self.labelContours5.setGeometry(QtCore.QRect(165, 90, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelContours5.setFont(font)
        self.labelContours5.setObjectName("labelContours5")
        self.groupBoxProcessed = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxProcessed.setGeometry(QtCore.QRect(1025, 0, 320, 230))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxProcessed.setFont(font)
        self.groupBoxProcessed.setObjectName("groupBoxProcessed")
        self.pictureBoxProcessed = QtWidgets.QLabel(self.groupBoxProcessed)
        self.pictureBoxProcessed.setGeometry(QtCore.QRect(14, 30, 291, 191))
        self.pictureBoxProcessed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictureBoxProcessed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pictureBoxProcessed.setLineWidth(1)
        self.pictureBoxProcessed.setText("")
        self.pictureBoxProcessed.setScaledContents(False)
        self.pictureBoxProcessed.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureBoxProcessed.setWordWrap(False)
        self.pictureBoxProcessed.setObjectName("pictureBoxProcessed")
        self.groupBoxRobot = QtWidgets.QGroupBox(self.tabRobotInteraction)
        self.groupBoxRobot.setGeometry(QtCore.QRect(1025, 410, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxRobot.setFont(font)
        self.groupBoxRobot.setObjectName("groupBoxRobot")
        self.textBoxIP = QtWidgets.QLineEdit(self.groupBoxRobot)
        self.textBoxIP.setGeometry(QtCore.QRect(10, 30, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textBoxIP.setFont(font)
        self.textBoxIP.setObjectName("textBoxIP")
        self.labelRobot1 = QtWidgets.QLabel(self.groupBoxRobot)
        self.labelRobot1.setGeometry(QtCore.QRect(165, 30, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRobot1.setFont(font)
        self.labelRobot1.setObjectName("labelRobot1")
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.groupBoxRobot)
        self.spinBoxSpeed.setEnabled(True)
        self.spinBoxSpeed.setGeometry(QtCore.QRect(10, 60, 77, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxSpeed.setFont(font)
        self.spinBoxSpeed.setMinimum(1)
        self.spinBoxSpeed.setMaximum(100)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.labelRobot2 = QtWidgets.QLabel(self.groupBoxRobot)
        self.labelRobot2.setGeometry(QtCore.QRect(90, 60, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRobot2.setFont(font)
        self.labelRobot2.setObjectName("labelRobot2")
        self.buttonInitPosition = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonInitPosition.setEnabled(True)
        self.buttonInitPosition.setGeometry(QtCore.QRect(1125, 520, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonInitPosition.setFont(font)
        self.buttonInitPosition.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonInitPosition.setStyleSheet("")
        self.buttonInitPosition.setAutoDefault(False)
        self.buttonInitPosition.setDefault(False)
        self.buttonInitPosition.setFlat(False)
        self.buttonInitPosition.setObjectName("buttonInitPosition")
        self.buttonDraw = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonDraw.setEnabled(True)
        self.buttonDraw.setGeometry(QtCore.QRect(1125, 560, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonDraw.setFont(font)
        self.buttonDraw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonDraw.setStyleSheet("")
        self.buttonDraw.setAutoDefault(False)
        self.buttonDraw.setDefault(False)
        self.buttonDraw.setFlat(False)
        self.buttonDraw.setObjectName("buttonDraw")
        self.buttonStop = QtWidgets.QPushButton(self.tabRobotInteraction)
        self.buttonStop.setEnabled(True)
        self.buttonStop.setGeometry(QtCore.QRect(1125, 600, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonStop.setFont(font)
        self.buttonStop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonStop.setStyleSheet("")
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
        self.groupBoxOperations.setTitle(_translate("MainWindow", "Operations"))
        self.buttonApply.setText(_translate("MainWindow", "Apply"))
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.label3.setText(_translate("MainWindow", "TextLabel"))
        self.label4.setText(_translate("MainWindow", "TextLabel"))
        self.label5.setText(_translate("MainWindow", "TextLabel"))
        self.buttonLoadImage.setText(_translate("MainWindow", "Load Image"))
        self.buttonTakePhoto.setText(_translate("MainWindow", "Take Photo"))
        self.buttonSaveImage.setText(_translate("MainWindow", "Save Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImageProcessing), _translate("MainWindow", "Image Processing"))
        self.groupBoxContours.setTitle(_translate("MainWindow", "Contours Detection"))
        self.labelContours1.setText(_translate("MainWindow", "Threshold"))
        self.labelContours3.setText(_translate("MainWindow", "Total number of contours "))
        self.labelContours4.setText(_translate("MainWindow", "Number of \"clean\" contours "))
        self.labelContours2.setText(_translate("MainWindow", "Screening area"))
        self.labelContours5.setText(_translate("MainWindow", "Approximation type"))
        self.groupBoxProcessed.setTitle(_translate("MainWindow", "Processed Image"))
        self.groupBoxRobot.setTitle(_translate("MainWindow", "Robot Parameters"))
        self.textBoxIP.setText(_translate("MainWindow", "10.10.10.20:8081"))
        self.labelRobot1.setText(_translate("MainWindow", "IP-adress"))
        self.labelRobot2.setText(_translate("MainWindow", "Speed"))
        self.buttonInitPosition.setText(_translate("MainWindow", "Init Position"))
        self.buttonDraw.setText(_translate("MainWindow", "Draw"))
        self.buttonStop.setText(_translate("MainWindow", "STOP!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRobotInteraction), _translate("MainWindow", "Robot Interaction"))
import Data.style_rc
