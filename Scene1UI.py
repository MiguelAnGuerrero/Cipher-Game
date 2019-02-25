import sys
#import Scene1
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot,QSize


class App(QWidget):


    def __init__(self):
        super().__init__()

        QWidget.__init__(self)

        oImage = QImage("Scene1.png")
        sImage = oImage.scaled(QSize(1920, 1080))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.title = 'Cipher Slueth'
        self.left = 10
        self.top = 10
        self.width = 1920
        self.height = 1080
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)


        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Access Computer', self)
        #button2 = QPushButton('Book!',self)

        button.setToolTip('')
        button.move(900, 500)
        button.clicked.connect(self.on_click)

        #button.setToolTip('')
        #button.move(130, 930)
        #button.clicked.connect(self.on_click)

        self.show()

        alert = QMessageBox()
        alert.setText('The prinipal has confiscated your cell phone and you should be recieving a message from this girl you like. You need to get the cell phone back! \n Look, there is a sticky note attached to the computer. Maybe it is the password, he really should not leave that out in the open. Anyone could log in and compromise his computer. Knowing that former CIA nut, I bet the password is encrypted.')
        alert.exec_()

    #@pyqtSlot()
    #def on_clickBook(self):
        #webbrowser.open('index.html')
    @pyqtSlot()
    def on_click(self):
      os.system("python Scene2UI.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
