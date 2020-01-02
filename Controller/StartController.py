from Controller.PhoneInputController import PhoneInputController
from View.PhoneInputView import PhoneInputView
from View.StartView import StartView


class StartController:
    def __init__(self):
        pass

    def show_form(self):
        self.startView = StartView()
        self.startView.switch_window.connect(self.show_phone_input)
        self.startView.show()

    def show_phone_input(self):
        self.startView.close()
        self.phone_input_controller = PhoneInputController()
        self.phone_input_controller.show_form()
