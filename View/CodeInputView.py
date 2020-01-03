from PyQt5 import QtWidgets, QtCore


class CodeInputView(QtWidgets.QWidget):
    sendCodeFromTextElementEvent = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Code input view')

        layout = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setGeometry(QtCore.QRect(760, 350, 400, 100))
        self.line_edit.setInputMask('9999')

        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton(self)
        self.button.clicked.connect(self.send_code_from_text_element)
        self.button.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.button.setText("SEND")

        layout.addWidget(self.button)

        self.showFullScreen()
        self.setLayout(layout)

    def send_code_from_text_element(self):
        self.sendCodeFromTextElementEvent.emit()