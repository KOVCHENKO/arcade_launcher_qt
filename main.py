from PyQt5 import QtWidgets

from View.StartView import StartView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartForm = QtWidgets.QWidget()
    ui = StartView()
    ui.setupUi(StartForm)
    StartForm.showFullScreen()
    StartForm.show()
    sys.exit(app.exec_())