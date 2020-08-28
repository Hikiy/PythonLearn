import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lab = QLabel(self)
        lineEdit = QLineEdit(self)

        self.lab.move(60, 40)
        lineEdit.move(60, 100)

        lineEdit.textChanged[str].connect(self.onChange)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChange(self, text):
        self.lab.setText(text)
        self.lab.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())