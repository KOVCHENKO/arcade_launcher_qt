from PyQt5 import QtCore, QtWidgets


class StartView(QtWidgets.QWidget):
    switchWindow = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Start View')
        self.resize(1920, 1080)

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton(self)
        self.button.clicked.connect(self.show_phone_input_view)
        self.button.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.button.setText("LOGIN")

        layout.addWidget(self.button)

        self.showFullScreen()
        self.setLayout(layout)

    def show_phone_input_view(self):
        self.switchWindow.emit()
