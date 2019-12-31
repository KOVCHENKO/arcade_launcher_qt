from PyQt5 import QtCore, QtWidgets


class PhoneInputView(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Phone Input')

        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('CONTINUE')
        self.button.setGeometry(QtCore.QRect(760, 500, 400, 100))

        # self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.showFullScreen()
        self.setLayout(layout)

    # def setupUi(self, Form):
    #     Form.setObjectName("Form")
    #     Form.resize(1920, 1080)
    #
    #     self.pushButton = QtWidgets.QPushButton(Form)
    #     self.pushButton.setGeometry(QtCore.QRect(760, 500, 400, 100))
    #     self.pushButton.setObjectName("pushButton")
    #     Form.setWindowTitle("PhoneInputForm")
    #     self.pushButton.setText("CONTINUE")
    #
    #     Form.showFullScreen()
    #     Form.hide()
    #     Form.show()