import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

#定义一个单击事件
def onClick_Button():
    print("方法一")
    print("widget.x() = %d" % widget.x()) #250 （窗口（含有标题栏）的左上角横坐标）
    print("widget.y() = %d" % widget.y()) #200 （窗口（含有标题栏）的左上角纵坐标）
    print("widget.width() = %d" % widget.width()) #300 (工作区域宽度)
    print("widget.height() = %d" % widget.height()) #240 （工作区域高度）

    print("方法二")  #通过坐标系
    print("widget.geometry().x() = %d" % widget.geometry().x()) #251 （工作区域（不包含标题栏）左上角横坐标）
    print("widget.geometry().y() = %d" % widget.geometry().y()) #252 （工作区域（不包含标题栏）左上角纵坐标）
    print("widget.geometry().width() = %d" % widget.geometry().width()) #300 (工作区域宽度)
    print("widget.geometry().height() = %d" % widget.geometry().height()) #240 （工作区域高度）

    print("方法三")  #
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x()) #250 （窗口（含有标题栏）的左上角横坐标）
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y()) #200 （窗口（含有标题栏）的左上角纵坐标）
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())  #302 (窗口宽度)
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())  #293 （窗口高度）

#使用面向过程的方式
app = QApplication(sys.argv)

#使用QWidget创建窗口
widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

#移动按钮到相应位置
btn.move(24,52)

#设置工作区的尺寸
widget.resize(300,240)

#移动窗口
widget.move(250,200)

widget.setWindowTitle("屏幕坐标系")

widget.show()

sys.exit(app.exec_()) #进入程序主循环防止退出

