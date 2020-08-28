from PyQt5.QtWidgets import (QWidget, QApplication, QGraphicsScene, QGraphicsView, QHBoxLayout, QGraphicsItem)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QRectF, qrand

import sys


class Butterfly(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.up = True

        self.pic = QPixmap('butterfly1.png')

    # 图元限定区域,以图元自身中心为坐标中心，类似图元占的大小
    def boundingRect(self):
        adjust = 2
        return QRectF(-self.pic.width() / 2 - adjust, -self.pic.height() / 2,
                      self.pic.width() + adjust * 2, self.pic.height() + adjust * 2)

    # 绘制
    def paint(self, painter, option, widget):
        painter.drawPixmap(self.boundingRect().topLeft(), self.pic)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 生成场景
        self.scene = QGraphicsScene()
        # 场景区域（左上角x坐标, 左上角y坐标, 宽, 高）
        self.scene.setSceneRect(-400, -250, 400, 500)

        # 这是一个QGraphicsItem类
        bf = Butterfly()
        # 这个是设置在scene的坐标
        bf.setPos(0, 0)

        # 场景中添加图元
        self.scene.addItem(bf)

        # 生成视图并添加场景
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        # 设置最小视图大小
        self.view.setMinimumSize(800, 500)

        self.boxLayout = QHBoxLayout()
        self.boxLayout.addWidget(self.view)
        self.setLayout(self.boxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    butterfly = MainWindow()
    butterfly.show()
    sys.exit(app.exec_())