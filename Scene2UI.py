import sys
#import Scene1
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot,QSize


class App(QWidget):


    def __init__(self):
        super().__init__()

        QWidget.__init__(self)

        oImage = QImage("UnlockComputer.png")
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

        button1 = QPushButton('Unlock Computer', self)
        button2 = QPushButton('Book!',self)

        button1.setToolTip('')
        button1.move(900, 500)
        button1.clicked.connect(self.on_click)

        button2.setToolTip('')
        button2.move(130, 930)
        button2.clicked.connect(self.on_clickBook)

        self.show()

        alert = QMessageBox()
        alert.setText('Hmmmm...this password seems to be encrypted. I should check my reference manual to see if I can break it. It kind of looks like a Caesar cipher with a shift of 3.')
        alert.exec_()


    @pyqtSlot()
    def on_click(self):
        os.system("python Scene3UI.py")

    @pyqtSlot()
    def on_clickBook(self):
        webbrowser.open('index.html')
        #os.system("C\\Program Files\\internet explorer\\iexplore.exe")


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
