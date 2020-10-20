from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")

        self.resize(300,320)

        # 创建TextEdit控件
        self.textEdit = QTextEdit()
        # 创建按钮
        self.buttonText = QPushButton("显示文本")
        self.buttonHTML = QPushButton("显示HTML")
        self.buttonToText = QPushButton("获取文本")
        self.buttonToHTML = QPushButton("获取HTML")

        layout = QVBoxLayout() # 创建垂直布局
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)

        self.setLayout(layout)

        # 把槽绑定到按钮的单击事件
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)


    # 编写槽
    def onClick_ButtonText(self):
        self.textEdit.setPlainText("HIHIHIHIHIHI") # 设置普通文本

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml("<font color='blue' size='5'>HIHIHIHIHIHI</font>")

    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHtml())


if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QTextEditDemo()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环









