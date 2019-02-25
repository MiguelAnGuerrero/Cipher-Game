#TITLE CARD

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import pyqtSlot,QSize


class App(QWidget):


    def __init__(self):
        super().__init__()

        QWidget.__init__(self)

        oImage = QImage("TitleScreen.png")
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

        button = QPushButton('Start Game!', self)
        button.setToolTip('')
        button.move(700, 700)
        button.clicked.connect(self.on_click)

        quitButton = QPushButton('Quit Game!', self)
        quitButton.setToolTip('')
        quitButton.move(1120, 700)
        quitButton.clicked.connect(self.quit_click)

        creditsButton = QPushButton('Credits', self)
        creditsButton.setToolTip('')
        creditsButton.move(915, 700)
        creditsButton.clicked.connect(self.credits_click)

        self.show()

    @pyqtSlot()
    def credits_click(self):
        alert = QMessageBox()
        alert.setText('Created By:\nRon, Luke, Christine, Miguel\nHackCU2019')
        alert.exec_()

    @pyqtSlot()
    def quit_click(self):
        print('PyQt5 button click')
        sys.exit(app.exec_())


    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        os.system('Scene1UI.py') #ALL THE JANK


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
sys.exit(app.exec_())