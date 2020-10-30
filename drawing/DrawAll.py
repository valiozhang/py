'''

绘制图形 DrawAll

弧形
圆形
椭圆
矩形
多边形
绘制图像

'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(400,800)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.blue)

        # 绘制弧
        # 绘制弧，弧是圆的特殊形式，定义弧绘制区域
        # 四个参数(左上角坐标，宽度，高度)
        rect = QRect(0,10,100,100)
        qp.drawArc(rect,0,50*16)               # (起始角度，结束角度)
                                               # alen:1个alen等于1/16度，45度：45*16alen

        # 通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0,360*16)    # 360度的弧就是圆
                                               # (坐标，宽度，高度，起始角度，结束角度)
        # 带弦的弧
        qp.drawChord(10,120,100,100,12,130*16) # 两个端点相连
                                               # (坐标，宽度，高度，起始角度，结束角度)
        # 绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)   # 两个端点与圆心相连
                                               # (坐标，宽度，高度，起始角度，结束角度)
        # 椭圆
        qp.drawEllipse(120,120,150,100)        # (坐标，宽度，高度),宽度高度相等的话就是圆

        # 绘制五边形
        # 指定五个点
        point1 = QPoint(140,380)
        point2 = QPoint(270,420)
        point3 = QPoint(290,512)
        point4 = QPoint(290,588)
        point5 = QPoint(200,533)
        # 创建多边形
        polygon = QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)

        # 绘制图像
        image = QImage('./image/a.png')         # 装载图像
        rect = QRect(10,600,image.width()/5,image.height()/5) # (窗口坐标,区域)，缩小到1/3
        qp.drawImage(rect,image)


        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())