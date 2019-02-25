import sys
#import Scene1
import os
from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton
from PyQt5.QtGui import * # QIcon
from PyQt5.QtCore import * # pyqtSlot


class App(QWidget):

    passcode = ''
    def __init__(self):
        super().__init__()

        QWidget.__init__(self)

        image = QImage('CabinetCode.png')
        image = image.scaled(QSize(1920, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(image))  # 10 = Windowrole

        self.setPalette(palette)
        self.title = 'Cipher Slueth'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()
        self.show()
        
        alert = QMessageBox()
        alert.setText("Finally I have reached our Phones. The gym teacher\'s encryption is hard, I\'m going to have to check and see my book for all the help i can get. This will be my toughest challenge as a Cipher Slueth! (Why is everyone leaving their password out in the open? That\'s not smart")
        alert.exec_()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        passcode = []
        correct_code = ['3', '4', '9', '1']
        button1 = QPushButton('1', self)
        button1.setToolTip('')
        button1.move(1393, 633)
        button1.resize(50, 30)
        button1.clicked.connect(lambda: add_value(passcode, '1'))

        button2 = QPushButton('2', self)
        button2.setToolTip('')
        button2.move(1479, 633)
        button2.resize(50, 30)
        button2.clicked.connect(lambda: add_value(passcode, '2'))

        button3 = QPushButton('3', self)
        button3.setToolTip('')
        button3.move(1558, 633)
        button3.resize(50, 30)
        button3.clicked.connect(lambda: add_value(passcode, '3'))

        button4 = QPushButton('4', self)
        button4.setToolTip('')
        button4.move(1393, 684)
        button4.resize(50, 30)
        button4.clicked.connect(lambda: add_value(passcode, '4'))

        button4 = QPushButton('5', self)
        button4.setToolTip('')
        button4.move(1479, 684)
        button4.resize(50, 30)
        button4.clicked.connect(lambda: add_value(passcode, '5'))

        button4 = QPushButton('6', self)
        button4.setToolTip('')
        button4.move(1558, 684)
        button4.resize(50, 30)
        button4.clicked.connect(lambda: add_value(passcode, '6'))

        button7 = QPushButton('7', self)
        button7.setToolTip('')
        button7.move(1393, 731)
        button7.resize(50, 30)
        button7.clicked.connect(lambda: add_value(passcode, '7'))

        button8 = QPushButton('8', self)
        button8.setToolTip('')
        button8.move(1479, 731)
        button8.resize(50, 30)
        button8.clicked.connect(lambda: add_value(passcode, '8'))

        button9 = QPushButton('9', self)
        button9.setToolTip('')
        button9.move(1558, 731)
        button9.resize(50, 30)
        button9.clicked.connect(lambda: add_value(passcode, '9'))

        button0 = QPushButton('0', self)
        button0.setToolTip('')
        button0.move(1638, 731)
        button0.resize(50, 30)
        button0.clicked.connect(lambda: add_value(passcode, '0'))

        enter_button = QPushButton('Enter', self)
        enter_button.setToolTip('')
        enter_button.move(1630, 684)
        enter_button.resize(59, 30)
        enter_button.clicked.connect(lambda: enter_button_clicked(passcode))

        clear_button = QPushButton('Clear', self)
        clear_button.setToolTip('')
        clear_button.move(1630, 633)
        clear_button.resize(59, 30)
        clear_button.clicked.connect(lambda: clear_button_clicked(passcode))

        def add_value(passcode, number):
            if len(passcode) < 4:
                passcode.append(number)
            else:
                print('Passcode is only 4 digits, hit enter')

        def enter_button_clicked(passcode):
            if passcode == correct_code:
                os.system("python EndScene.py")

            else:
                clear_button_clicked()

            return

        def clear_button_clicked(passcode):
            for i in range(len(passcode)):
                passcode.pop()
            print(passcode)
            return passcode


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())