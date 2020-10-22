"""
计数器控件 QSpinBox
如何使用：
显示数字，获取数字，捕获变化的信号
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QSpinBox演示") # 设置标题
        self.resize(500,100)

        layout = QVBoxLayout()
        self.label = QLabel("当前值") # 创建一个标签
        self.label.setAlignment(Qt.AlignCenter) #设置居中

        layout.addWidget(self.label) # 把控件添加到布局

        self.sb = QSpinBox() # 创建控件
        self.sb.setValue(18) # 设置默认值
        self.sb.setRange(10,40) # 设置范围
        self.sb.setSingleStep(3) # 设置步长（每次增3）
        layout.addWidget(self.sb)
        # 绑定信号和槽
        self.sb.valueChanged.connect(self.valueChange) # 信号是valuechanged，当值变化时触发
        self.setLayout(layout)

    # 编写槽
    def valueChange(self):
        self.label.setText("当前值：" + str(self.sb.value()))
        # 注意：self.sb.value()是方法，不是属性，记得加括号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())

