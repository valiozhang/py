"""
A ASCII字母字符是必须输入的(A-Z、a-z)
a ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)
N ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)
X 任何字符都是必须输入的
x 任何字符都是允许输入的,但不是必需的
9 ASCII数字字符是必须输入的(0-9)
0 ASCII数字字符是允许输入的,但不是必需的(0-9)
D ASCII数字字符是必须输入的(1-9)
d ASCII数字字符是允许输入的,但不是必需的(1-9)
# ASCI数字字符或加减符号是允许输入的,但不是必需的
H 十六进制格式字符是必须输入的(A-F、a-f、0-9)
h 十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
B 二进制格式字符是必须输入的(0,1)
b 二进制格式字符是允许输入的,但不是必需的(0,1)
> 所有的字母字符都大写
< 所有的字母字符都小写
! 关闭大小写转换
\ 使用""转义上面列出的字符
"""

from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("用掩码限制QLineEdit控件的输入")
        formLayout = QFormLayout()

        # 创建控件
        ipLineEdit = QLineEdit() # 限制IP
        pcLineEdit = QLineEdit() # 限制主机地址
        dateLineEdit = QLineEdit() # 输入日期
        licenseLineEdit = QLineEdit() # 输入许可证序列号

        # 设置掩码 .setInputMask(“”)
        ipLineEdit.setInputMask("000.000.000.000;_") # 192.168.21.45,没有输入时0显示为_
        pcLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_") # 用16进制表示,没有输入时0显示为_
        dateLineEdit.setInputMask("0000-00-00") #限制日期
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#") # 没有输入时0显示为#

        formLayout.addRow("数字掩码",ipLineEdit)
        formLayout.addRow("主机掩码",pcLineEdit)
        formLayout.addRow("日期掩码",dateLineEdit)
        formLayout.addRow("许可证掩码",licenseLineEdit)

        # 设置布局
        self.setLayout(formLayout)

if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QLineEditMask()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环


