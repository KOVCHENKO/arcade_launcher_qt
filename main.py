import sys

from PyQt5 import QtWidgets

from Controller.StartController import StartController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = StartController()
    controller.show_form()
    sys.exit(app.exec_())
