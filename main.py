import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QGridLayout,QPushButton)
from PyQt5.QtWidgets import (QMainWindow,QAction,qApp,QMenu,QTextEdit)
from PyQt5.QtGui import QIcon
import os



class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        '''
        批量上传UI布局
        '''

        # grid = QGridLayout()
        # self.setLayout(grid)
        
        # nameMenu = ['文件','编辑','Excel','数据库','远程连接','人脸128']

        # positions = [(i,j) for i in range(1) for j in range(6)]
        
        # for position, name in zip(positions, nameMenu):

        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     print(position)
        #     grid.addWidget(button, *position)

        # buttons = QPushButton('工具栏')
        # grid.addWidget(buttons,*(1,0))

        self.move(640, 480)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())