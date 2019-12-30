import sys

from PyQt5 import QtWidgets
from View.PhoneInputView import PhoneInputView


class StartController:
    def __init__(self):
        self.previousForm = None

    def saySomething(self):
        print("Say something in start controller")
        # self.previousForm.hide()

        # app = QtWidgets.QApplication(sys.argv)
        PhoneInputForm = QtWidgets.QWidget()
        print(PhoneInputForm)
        ui = PhoneInputView()
        ui.setupUi(self.previousForm)