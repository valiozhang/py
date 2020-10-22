'''
对话框：QDialog

消息对话框 QMessageBox
颜色对话框 QColorDialog
打开/保存对话框 QFileDialog
设置字体对话框 QFontDialog
获取输入信息对话框 QInputDialog

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialog案例")
        self.resize(500,300)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(100,100)
        self.button.clicked.connect(self.showDialog)

    # 创建显示对话框的函数
    def showDialog(self):
        dialog = QDialog()
        button = QPushButton("确定",dialog)
        button.clicked.connect(dialog.close)
        dialog.setWindowTitle("对话框")
        # 设置对话框以模式状态显示
        dialog.setWindowModality(Qt.ApplicationModal) # 当对话框显示时，QMainWindow里的控件都不可用

        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
