from PyQt5 import QtCore, QtWidgets


class PhoneInputView(QtWidgets.QWidget):
    send_phone_from_text_element_event = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Phone Input')

        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setGeometry(QtCore.QRect(760, 350, 400, 100))
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton(self)
        self.button.clicked.connect(self.send_phone_from_text_element)
        self.button.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.button.setText("SEND")

        # self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.showFullScreen()
        self.setLayout(layout)

    def send_phone_from_text_element(self):
        self.send_phone_from_text_element_event.emit()