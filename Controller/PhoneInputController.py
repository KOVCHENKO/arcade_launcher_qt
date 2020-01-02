from View.PhoneInputView import PhoneInputView


class PhoneInputController:
    def __init__(self):
        pass

    def show_form(self):
        self.phoneInputView = PhoneInputView()
        self.phoneInputView.send_phone_from_text_element_event.connect(self.send_phone_number)
        self.phoneInputView.show()

    def send_phone_number(self):
        phone_number_text = self.phoneInputView.line_edit.text()
        print("phone number has been sent")
        print(phone_number_text)