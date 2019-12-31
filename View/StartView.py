from PyQt5 import QtCore, QtWidgets


class StartView(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Start View')
        self.resize(1920, 1080)

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.show_phone_input_view)
        self.button.setGeometry(QtCore.QRect(760, 500, 400, 100))

        layout.addWidget(self.button)

        self.showFullScreen()
        self.setLayout(layout)

    def show_phone_input_view(self):
        self.switch_window.emit()

    # def setupUi(self, Form):
    #     self.pushButton = QtWidgets.QPushButton(Form)
    #     self.pushButton.setGeometry(QtCore.QRect(760, 500, 400, 100))
    #     self.pushButton.setObjectName("pushButton")
    #
    #     self.startController.previousForm = Form
    #     self.pushButton.clicked.connect(self.startController.saySomething)
    #     self.pushButton.setText("START")
    #     Form.setWindowTitle("START FORM")
    #     Form.showFullScreen()
    #     Form.show()
