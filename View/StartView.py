from PyQt5 import QtCore, QtWidgets

from Controller.StartController import StartController

class StartView():
    def __init__(self):
        self.startController = StartController()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.pushButton.setObjectName("pushButton")

        self.startController.previousForm = Form
        self.pushButton.clicked.connect(self.startController.saySomething)
        self.pushButton.setText("START")
        Form.setWindowTitle("START FORM")
        Form.showFullScreen()
        Form.show()


