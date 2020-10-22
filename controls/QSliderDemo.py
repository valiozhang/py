"""
滑块空间QSlider
通过滑块左右拉动控制数字变化
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(500,700)
        layout = QVBoxLayout()
        self.label = QLabel('你好 PyQt5')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.slider = QSlider(Qt.Horizontal) # 创建水平滑块对象
        self.slider.setMinimum(12) # 设置最小值
        self.slider.setMaximum(48) # 设置最大值
        self.slider.setSingleStep(3) # 步长
        self.slider.setValue(18) # 设置当前值
        self.slider.setTickPosition(QSlider.TicksBelow) # 设置刻度的位置，刻度在下方
        self.slider.setTickInterval(6) # 设置刻度的间隔
        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange) # 绑定槽
        self.slider1 = QSlider(Qt.Vertical)
        layout.addWidget(self.slider1)
        self.slider1.setMinimum(10) # 设置最小值
        self.slider1.setMaximum(60) # 设置最大值
        self.slider1.setSingleStep(5) # 设置步长
        self.slider1.setValue(30) # 设置当前值
        self.slider1.setTickPosition(QSlider.TicksLeft) # 设置刻度的位置，刻度在下方
        self.slider1.setTickInterval(2) # 设置刻度的间隔
        self.slider1.valueChanged.connect(self.valueChange) # 绑定槽
        self.setLayout(layout)

    # 编写槽
    def valueChange(self):
        print('当前值：%s' % self.sender().value()) # 获得当前的数字值
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size)) # 通过数字的值改变字号


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())