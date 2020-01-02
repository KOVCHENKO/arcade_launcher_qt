from Service.PhoneInputService import PhoneInputService
from View.PhoneInputView import PhoneInputView


class PhoneInputController:
    phoneInputService: PhoneInputService
    phoneNumberText: str
    phoneInputView: PhoneInputView

    def __init__(self):
        self.phoneInputView = PhoneInputView()
        self.phoneInputService = PhoneInputService()

    def show_form(self):
        self.phoneInputView.sendPhoneFromTextElementEvent.connect(self.send_phone_number)
        self.phoneInputView.show()

    def send_phone_number(self):
        self.phoneNumberText = self.phoneInputView.line_edit.text()
        self.phoneInputService = self.phoneInputService.send_phone(self.phoneNumberText)