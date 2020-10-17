import sys
#使用水平布局QHbox...,添加QPush,添加控件QWidget
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

#编写类
class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")

        #添加Button
        self.button1 = QPushButton("退出应用程序")
        #将信号与槽关联，将button的clicked信号绑定到槽上，发送单击信号，就会执行槽对应的方法
        self.button1.clicked.connect(self.onClick_Button)

        #把按钮放到窗口上，需要放一个布局，此时选择水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1) #把控件button添加到布局里

        #需要一个主框架，把所有控件放到QWidget上
        mainFrame = QWidget()
        mainFrame.setLayout(layout) #把布局放到主框架里

        self.setCentralWidget(mainFrame) #把主框架放到整个窗口上，充满整个屏幕


    #编写按钮单击事件的方法（相当于自定义的槽）
    def onClick_Button(self):
        sender = self.sender() #发送对象，通过sender获得button
        print(sender.text() + "按钮被按下") #text是把button的文本输入
        app = QApplication.instance() #得到实例，QApplication对象的指针可以通过instance()函数获取
        #退出应用程序
        app.quit()

if __name__ == "__main__": #防止别的脚本调用
    app = QApplication(sys.argv) #传入参数
    main = QuitApplication() #创建类
    main.show() #调用show来显示
    sys.exit(app.exec_()) #进入程序的主循环


