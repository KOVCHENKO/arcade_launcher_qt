from Controller.PhoneInputController import PhoneInputController
from View.StartView import StartView


class StartController:
    phoneInputController: PhoneInputController
    startView: StartView

    def __init__(self):
        pass

    def show_form(self):
        self.startView = StartView()
        self.startView.switchWindow.connect(self.show_phone_input)
        self.startView.show()

    def show_phone_input(self):
        self.startView.close()
        self.phoneInputController = PhoneInputController()
        self.phoneInputController.show_form()
