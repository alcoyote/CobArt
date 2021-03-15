from main_form import CobArt
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    f = CobArt()
    f.show()
    app.exec_()
