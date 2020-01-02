from View.PhoneInputView import PhoneInputView


class PhoneInputController:
    phoneNumberText: str
    phoneInputView: PhoneInputView

    def __init__(self):
        self.phoneInputView = PhoneInputView()

    def show_form(self):
        self.phoneInputView.sendPhoneFromTextElementEvent.connect(self.send_phone_number)
        self.phoneInputView.show()

    def send_phone_number(self):
        self.phoneNumberText = self.phoneInputView.line_edit.text()

        print("phone number has been sent")
        print(self.phoneNumberText)