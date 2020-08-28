from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsScene, QGraphicsView, QHBoxLayout, QGraphicsItem)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QRectF, qrand

import sys
import math


class Butterfly(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.up = True

        self.bfUp = QPixmap('butterfly1.png')
        self.bfDown = QPixmap('butterfly2.png')

        self.timer = QTimer()
        self.timer.timeout.connect(self.fly)
        self.timer.start(100)

        self.angle = 0

    # 图元限定区域,以图元自身中心为坐标中心，类似图元占的大小
    def boundingRect(self):
        adjust = 2
        # print(-self.bfUp.width() / 2 - adjust, -self.bfUp.height() / 2,
        #               self.bfUp.width() + adjust * 2, self.bfUp.height() + adjust * 2)
        return QRectF(-self.bfUp.width() / 2 - adjust, -self.bfUp.height() / 2,
                      self.bfUp.width() + adjust * 2, self.bfUp.height() + adjust * 2)

    def paint(self, painter, option, widget):
        if self.up:
            painter.drawPixmap(self.boundingRect().topLeft(), self.bfUp)
        else:
            painter.drawPixmap(self.boundingRect().topLeft(), self.bfDown)
        self.up = not self.up

    def fly(self):
        # edgex = self.scene().sceneRect().right() + self.boundingRect().width() / 2
        edgex = self.scene().sceneRect().left() - self.boundingRect().width() / 2
        edgetop = self.scene().sceneRect().top() + self.boundingRect().height() / 2
        edgebottom = self.scene().sceneRect().bottom() + self.boundingRect().height() / 2

        # if (self.pos().x() >= edgex):
        #     self.setPos(self.scene().sceneRect().left(), self.pos().y())
        if self.pos().x() <= edgex:
            self.setPos(self.scene().sceneRect().right(), self.pos().y())
        if self.pos().y() <= edgetop:
            self.setPos(self.pos().x(), self.scene().sceneRect().bottom())
        if self.pos().y() >= edgebottom:
            self.setPos(self.pos().x(), self.scene().sceneRect().top())

        self.angle += (qrand() % 10) / 20.0
        dx = math.fabs(math.sin(self.angle * math.pi) * 10.0)
        dy = (qrand() % 20) - 10.0
        # self.setPos(self.mapToParent(self.dx, self.dy))
        self.setPos(self.mapToParent(-dx, dy))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-400, -250, 400, 500)

        bf = Butterfly()
        bf.setPos(0, 0)

        self.scene.addItem(bf)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setMinimumSize(800, 500)

        self.boxLayout = QHBoxLayout()
        self.boxLayout.addWidget(self.view)
        self.setLayout(self.boxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    butterfly = MainWindow()
    butterfly.show()
    sys.exit(app.exec_())
