import sys
#从PyQt5.QtWidgets包里导入，通过类：QDesktopWidget获取屏幕尺寸
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon #QIcon添加图标

#编写和所有UI有关的类
class CenterForm(QMainWindow):
    # 构造函数，在此函数里初始化，保证QMainWindow是主窗口,由此此时默认，可以把parent去掉
    def __init__(self,parent=None):
        super(CenterForm,self).__init__(parent)

        #设置主窗口标题
        self.setWindowTitle("让窗口居中")

        #设置窗口尺寸
        self.resize(400,300)

    def center(self): #定义一个函数让窗口居中显示
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        #移动窗口
        self.move(int(newLeft),int(newTop)) #防计算结果为浮点数导致调用move函数时报错


if __name__ == "__main__": #防止别的脚本调用
    app = QApplication(sys.argv) #传入参数
    main = CenterForm() #创建类
    main.center() #调用函数
    main.show() #调用show来显示

    sys.exit(app.exec_()) #进入程序的主循环



