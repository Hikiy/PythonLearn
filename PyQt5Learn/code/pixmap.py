from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pic = QPixmap('butterfly1.png')

        lab = QLabel()
        lab.setPixmap(pic)

        hBox = QHBoxLayout(self)
        hBox.addWidget(lab)
        self.setLayout(hBox)

        self.move(300, 300)
        self.setWindowTitle("butterfly")
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
