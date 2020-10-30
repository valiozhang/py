'''
绘制不同的直线
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class DrawMultiline(QWidget):
    def __init__(self):
        super(DrawMultiline, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()                # 创建画板

        painter.begin(self)

        pen = QPen(Qt.red,3,Qt.SolidLine)   # 创建画笔，有三个参数：颜色，粗细，实线
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)           # 虚线
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)        # 点画线
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)            # 窄虚线
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)     # 两点画线
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20, 180, 250, 180)

        # 自定义
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,10,20])     # 设置线的模式
                                            # 自定义点画线风格[第1个线段宽度，间隔宽度，第2个线段宽度，间隔宽度]
        painter.setPen(pen)                 # 设置完样式要set才能生效
        painter.drawLine(20, 240, 250, 240)

        size = self.size()

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiline()
    main.show()
    sys.exit(app.exec_())