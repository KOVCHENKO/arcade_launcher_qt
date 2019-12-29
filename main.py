import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class mainUI(QWidget):
    def __init__(self):
        super(mainUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.showFullScreen()

        qbtn = QPushButton('Quit')
        qbtn.clicked.connect(QtCore.QCoreApplication.quit)
        qbtn.move(50, 50)
        self.button = qbtn
        qbtn.show()

def main():
    app = QApplication(sys.argv)
    window = mainUI()
    window.__init__()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()