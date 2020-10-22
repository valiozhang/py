"""
下拉列表控件QComboBox
1.如何将列表项添加到QComboBox控件中
2.如何获取选中的列表项
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300,100)

        layout = QVBoxLayout() # 设置垂直布局

        # 显示编程语言
        self.label = QLabel("请选择编程语言")

        # 创建ComBox对象
        self.cb = QComboBox()
        # 添加编程语言
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["Java","C#","Ruby"]) # 一次添加多个选项

        # 绑定信号和槽,ComboBox的信号是currentIndexChanged，获取当前选中元素的索引
        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self,i): #这个槽的两个参数都是自动传过来的，默认传递控件本身和索引
        self.label.setText(self.cb.currentText()) # 获取当前选择的文本
        self.label.adjustSize() # 根据文本来调整尺寸

        # 输出combobox里面所有的项来看他们的状态
        for count in range(self.cb.count()): #获取所有元素
            # self.cb.itemText(count)根据项的索引得到当前项的文本
            print("item" + str(count) + "=" + self.cb.itemText(count))
            # 输出多少项（i）,选择当前的状态（self.cb.currentText()）
            print("current index",i,"selection changed",self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())