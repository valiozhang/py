"""
mainLayout.addWidget(控件对象，rowIndex,columnIndex,row,column)
rowIndex行索引
columnIndex列索引
row占用多少行
column占用多少列
"""

from PyQt5.QtWidgets import * # 所有的都导入
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件") # 设置标题

        # 创建label和line控件
        nameLabel = QLabel("&Name",self) # 添加热键:&后面的英文字母就变成了热键（ALT+字母）
        nameLineEdit = QLineEdit(self)
        # 设置伙伴关系
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel("&Password", self)  # 添加热键:&后面的英文字母就变成了热键（ALT+字母）
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴关系
        passwordLabel.setBuddy(passwordLineEdit)

        # 创建按钮
        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")

        # 设置布局
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0) # 第一行，第一列
        mainLayout.addWidget(nameLineEdit,0,1,1,2) # 第一行，第二列，占用一行两列

        mainLayout.addWidget(passwordLabel,1,0) # 第二行，第一列
        mainLayout.addWidget(passwordLineEdit,1,1,1,2) # 第二行，第二列

        mainLayout.addWidget(btnOK,2,1) # 第三行，第一列
        mainLayout.addWidget(btnCancel,2,2) #第三行，第三列

if __name__ == "__main__": # 防止别的脚本调用
    app = QApplication(sys.argv) # 传入参数
    main = QLabelBuddy()
    main.show() # 调用show来显示
    sys.exit(app.exec_()) # 进入程序的主循环

