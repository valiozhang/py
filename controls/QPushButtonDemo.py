"""
父类 QAbstracButton
子类 QPushButton 一般按钮
    QToolButton 工具条按钮
    QRadioButton 单选按钮
    QCheckBox 多选按钮
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")

        layout = QVBoxLayout()

        self.button1 = QPushButton("第一个按钮")
        self.button1.setText("First Button1")
        self.button1.setCheckable(True) # 设置核对状态（按钮自动抬起）
        self.button1.toggle() # 设置开关
        # 绑定信号和槽的方法一
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        # 绑定信号和槽的方法二
        # 多个信号绑定到一个槽,当绑定多个槽时，对于不同的槽按照顺序进行调用
        self.button1.clicked.connect(self.buttonState)

        layout.addWidget(self.button1)

        # 在文本前面显示图像
        self.button2 = QPushButton("图像按钮")
        self.button2.setIcon(QIcon(QPixmap("./images/python.png")))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)

        # 让按钮不可用
        self.button3 = QPushButton("不可用的按钮")
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        #设置默认按钮（按回车自动调用）
        self.button4 = QPushButton("&MyButton")
        self.button4.setDefault(True) # 默认按钮一个窗口只能有一个
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked(): # 判断按钮是否被选中
            print("按钮1已被选中")
        else:
            print("按钮1未被选中")


    # 编写槽
    def whichButton(self,btn): # 确认按了哪个按钮
        print("被单击的按钮是<" + btn.text() + ">")


if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QPushButtonDemo()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环