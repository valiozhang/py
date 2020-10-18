"""
限制QLineEdit控件的输入（校验器）

限制只能输入整数、浮点数或满足一定条件的字符串
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")

        # 创建表单布局
        formLayout = QFormLayout()

        # 创建三个文本输入框，分别输入整数类型、浮点值类型和满足表达式的字符串
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        # 把上面的文本框添加到表单布局
        formLayout.addRow("整数类型",intLineEdit)
        formLayout.addRow("浮点类型",doubleLineEdit)
        formLayout.addRow("数字和字母",validatorLineEdit)

        # 设置提示文本
        intLineEdit.setPlaceholderText("整数类型")
        doubleLineEdit.setPlaceholderText("浮点类型")
        validatorLineEdit.setPlaceholderText("数字和字母")

        # 整数校验器 [1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99) # 范围

        #浮点校验器 [-360,360]，精度小数点后两位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360) # 范围
        # 标准的记号表示法，正常的表示浮点数
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点后两位
        doubleValidator.setDecimals(2)

        # 数字和字母校验器
        reg = QRegExp("[A-Za-z0-9]+$") # QRegExp是Qt的正则表达式
        validator = QRegExpValidator(self)
        validator.setRegExp(reg) # 正则表达式和正则计算器绑定

        # 把校验器和文本输入控件绑定
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        # 设置布局
        self.setLayout(formLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())













