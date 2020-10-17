import sys
#从PyQt5.QtWidgets包里导入，QMainWindow和QApplication是必须写的
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon #QIcon添加图标
"""
当窗口在windows中运行时，也会在工具栏具有一个图标，
如果希望能够在工具栏也显示对应的图标，需要调用系统函数，告诉系统需要显示图标：
"""
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
"""
窗口的setWindowIcon方法用于设置窗口的图标，只在windows中可用。
QApplication中的setWindowIcon用于设置主窗口图标和应用程序图标，但如果调用了窗口的setWindowIcon方法，
QApplication中的setWindowIcon方法就只能用于设置应用程序图标
"""

#编写和所有UI有关的类
class IconForm(QMainWindow):
    # 构造函数，在此函数里初始化，保证QMainWindow是主窗口,由此此时默认，可以把parent去掉
    def __init__(self):
        super(IconForm,self).__init__()
        self.initUI()

    def initUI(self): #把初始化单独放在一个函数里

        #设置窗口尺寸和位置
        self.setGeometry(300,300,250,250)
        #设置主窗口标题
        self.setWindowTitle("设置窗口图标")
        #设置窗口图标
        self.setWindowIcon(QIcon("./images/Basilisk.ico"))


if __name__ == "__main__": #防止别的脚本调用
    app = QApplication(sys.argv) #传入参数

    # 设置应用程序图标
    app.setWindowIcon(QIcon("./images/Dragon.ico"))
    main = IconForm() #创建类
    main.show() #调用show来显示

    sys.exit(app.exec_()) #进入程序的主循环



