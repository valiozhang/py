'''

用像素点绘制正弦函数

-2PI  2PI

drawPoint(x,y)

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('在窗口上用像素点绘制两个周期的正弦曲线')

    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        for i in range(1000): # 1000次循环，绘制1000个点
            # 计算绘图点的坐标
            x = 100 * (-1 + 2.0 * i/1000) + size.width()/2.0
            # 为什么加上size.width()/2.0：把屏幕水平的中心作为坐标轴原点
            y = -50 * math.sin((x - size.width()/2.0) * math.pi/50) + size.height()/2.0
            painter.drawPoint(x,y)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawPoints()
    main.show()
    sys.exit(app.exec_())