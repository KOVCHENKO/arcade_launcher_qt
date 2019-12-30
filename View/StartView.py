from PyQt5 import QtCore, QtWidgets

from Controller.StartController import StartController

class StartView():
    def __init__(self):
        self.startController = StartController

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(760, 500, 400, 100))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.startController.saySomething)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "START"))
