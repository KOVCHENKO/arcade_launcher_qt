from View.PhoneInputView import PhoneInputView


class StartController:
    def __init__(self):
        self.previousForm = None

    def saySomething(self):
        print("Say something in start controller")
        self.previousForm.hide()

        ui = PhoneInputView()
        ui.setupUi(self.previousForm)