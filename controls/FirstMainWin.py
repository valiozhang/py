import sys
#从PyQt5.QtWidgets包里导入，QMainWindow和QApplication是必须写的
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon #QIcon添加图标

#编写和所有UI有关的类
class FirstMainWin(QMainWindow):
    # 构造函数，在此函数里初始化，保证QMainWindow是主窗口,由此此时默认，可以把parent去掉
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #设置主窗口标题
        self.setWindowTitle("第一个主窗口应用")

        #设置窗口尺寸
        self.resize(400,300)

        #获得状态栏
        self.status = self.statusBar()

        #在状态栏显示消息
        self.status.showMessage("只存在5秒的消息",5000) #5000毫秒

if __name__ == "__main__": #防止别的脚本调用
    app = QApplication(sys.argv) #传入参数

    app.setWindowIcon(QIcon("./images/Dragon.ico")) #设置应用程序图标
    main = FirstMainWin() #创建类
    main.show() #调用show来显示

    sys.exit(app.exec_()) #进入程序的主循环



