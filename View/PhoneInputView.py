from PyQt5 import QtCore, QtWidgets


class PhoneInputView():
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.pushButton.setObjectName("pushButton")
        Form.setWindowTitle("PhoneInputForm")
        self.pushButton.setText("CONTINUE")

        Form.showFullScreen()
        Form.hide()
        Form.show()