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

        oImage = QImage("Scene2NoteOpen.png")
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

        button1 = QPushButton('To the Football Field', self)


        button1.setToolTip('')
        button1.move(400, 100)
        button1.clicked.connect(self.on_click)



        self.show()

        alert = QMessageBox()
        alert.setText('This note is encrypted again. What a nut! These numbers look sort of like ASCII values. I wonder if this is a simple number substitution?')
        alert.exec_()

    @pyqtSlot()
    def on_click(self):
      os.system("python Scene5UI.py") #SO JANKy
      


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
