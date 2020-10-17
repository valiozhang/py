#显示控件提示信息

import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
#给提示信息设置字体
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI() #调用初始化UI的方法

    #编写初始化UI的方法
    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",12)) #为类设置字体字号
        self.setToolTip("yayayayayayaya") #先给窗口设置提示，设置粗体
        self.setGeometry(300,300,200,300)
        self.setWindowTitle("设置控件提示消息")

        # 添加Button
        self.button1 = QPushButton("don't Push")
        self.button1.setToolTip("pigpigpigpigpigpig")
        # 把按钮放到窗口上，需要放一个布局，此时选择水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)  # 把控件button添加到布局里

        # 需要一个主框架，把所有控件放到QWidget上
        mainFrame = QWidget()
        mainFrame.setLayout(layout)  # 把布局放到主框架里
        self.setCentralWidget(mainFrame)  # 把主框架放到整个窗口上，充满整个屏幕

if __name__ == "__main__": #防止别的脚本调用
    app = QApplication(sys.argv) #传入参数
    main = TooltipForm() #创建类
    main.show() #调用show来显示
    sys.exit(app.exec_()) #进入程序的主循环

