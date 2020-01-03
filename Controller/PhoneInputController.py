from Controller.CodeInputController import CodeInputController
from Service.PhoneInputService import PhoneInputService
from View.PhoneInputView import PhoneInputView


class PhoneInputController:
    phoneInputService: PhoneInputService
    phoneNumberText: str
    phoneInputView: PhoneInputView

    def __init__(self):
        self.phoneInputView = PhoneInputView()
        self.phoneInputService = PhoneInputService()
        self.codeInputController = CodeInputController()

    def show_form(self):
        self.phoneInputView.sendPhoneFromTextElementEvent.connect(self.send_phone_number)
        self.phoneInputView.show()

    def send_phone_number(self):
        self.phoneNumberText = self.phoneInputView.line_edit.text()
        result = self.phoneInputService.resolve_phone_request(self.phoneNumberText)

        if result:
            self.codeInputController.show_form()