'''
文件对话框 QFileDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        # 显示加载的文本内容
        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框演示')

    def loadImage(self):
        # 第三个参数是路径，第四个是默认的文件格式
        # 两个返回参数，第二个是'是否点击退出'
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile) # 设置打开文件格式，此处是打开所有文件
        dialog.setFilter(QDir.Files) # 过滤

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0],encoding='utf-8',mode='r') # 打开第一个文件
            with f:                       # 防止忘了关闭文件，当with语句结束后，自动调用f中的close关闭文件
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
