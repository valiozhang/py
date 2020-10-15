import sys
import MainWinContainerLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)#创建Qapplication对象表示应用程序
    mainWindow = QMainWindow()#创建主窗口
    ui = MainWinContainerLayout.Ui_MainWindow()#引用自动生成的Ui_MainWindow类
    ui.setupUi(mainWindow)#调用setuiUi方法，向主窗口添加控件
    mainWindow.show()
    sys.exit(app.exec_())#运行主循环





