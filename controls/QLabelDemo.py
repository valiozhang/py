'''
QLabel控件

setAlignment()：设置文本的对齐方式

setIndent()：设置文本缩进

text()：获取文本内容

setBuddy()：设置伙伴关系

setText()：设置文本内容

selectedText()：返回所选择的字符

setWordWrap()：设置是否允许换行

QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发：linkHovered
2.  当鼠标单击QLabel控件时触发：linkActivated
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QToolTip,QLabel,QWidget
# 设置Label的背景色
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 设置标签1
        # 设置文本
        label1.setText("<font color=yellow>睡前读个故事吧！</font>")
        # 用调色板自动填充背景
        label1.setAutoFillBackground(True)
        # 创建调色板
        palette = QPalette()
        # 设置背景色
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        # 设置文本居中对齐
        label1.setAlignment(Qt.AlignCenter)

        # 设置标签2
        # 设置一个链接
        label2.setText("<a href='#'>给小屁推荐一本故事书</a>")

        # 设置标签3
        # 设置居中
        label3.setAlignment(Qt.AlignCenter)
        # 设置提示文本
        label3.setToolTip("这是一个图片标签")
        # 设置显示图片
        label3.setPixmap(QPixmap("./images/book.png"))

        # 设置标签4
        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        # 设置一个链接
        label4.setText("<a href='https://item.jd.com/12606236.html'>亲爱的小孩，猜猜世界多有趣</a>")
        # 设置右对齐
        label4.setAlignment(Qt.AlignRight)
        # 设置提示文本
        label4.setToolTip("这是一个网页链接")

        # 垂直布局
        vbox = QVBoxLayout()
        # 放到窗口上
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 绑定信号和槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        # 添加布局
        self.setLayout(vbox)
        # 设置标题
        self.setWindowTitle("QLabel控件演示")


    # 设置槽
    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")
    def linkClicked(self):
        print("当鼠标单击label4标签时，触发事件")

if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QLabelDemo()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环