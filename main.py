import sys

from PyQt5 import QtWidgets

from View.StartView import StartView

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StartForm = QtWidgets.QWidget()
    ui = StartView()
    ui.setupUi(StartForm)
    sys.exit(app.exec_())