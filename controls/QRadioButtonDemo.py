from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton")
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonState) # 选中未选中实际是状态切换的信号
        layout.addWidget(self.button1)

        self.button2 = QRadioButton("单选按钮2")
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    # 按钮选中状态
    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print("<" + radioButton.text() + "> 被选中")
        else:
            print("<" + radioButton.text() + "> 未被选中")



if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QRadioButtonDemo()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环