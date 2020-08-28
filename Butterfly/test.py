from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QBasicTimer

import sys

class Butterfly(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        bf1 = QPixmap('butterfly1.png')
        bf2 = QPixmap('butterfly2.png')

        self.lab1 = QLabel(self)
        self.lab2 = QLabel(self)

        self.lab1.setPixmap(bf1)
        self.lab2.setPixmap(bf2)
        self.lab1.move(1000, 150)
        self.lab2.move(1050, 250)
        self.lab2.hide()

        self.timer = QBasicTimer()
        self.timer.start(1000, self)

        self.setGeometry(300, 150, 1200, 800)
        self.setWindowTitle("飞舞的蝴蝶")
        self.show()

    def fly(self):
        if self.lab2.x() >= 0 and self.lab1.x() >= 0:
            if self.lab2.isHidden():
                self.lab1.hide()
                self.lab2.move(self.lab1.x() - 50, self.lab2.y())
                self.lab2.show()
            else:
                self.lab2.hide()
                self.lab1.move(self.lab2.x() - 50, self.lab1.y())
                self.lab1.show()
        else:
            self.lab1.move(1000, 150)
            self.lab2.move(1050, 250)

    def timerEvent(self, e):
        self.fly()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    butterfly = Butterfly()
    sys.exit(app.exec_())
