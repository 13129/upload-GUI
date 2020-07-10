import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget)
from PyQt5.QtGui import (QIcon,QFont)
from PyQt5.QtCore import QCoreApplication
import os




# print('目录',os.path.abspath(os.path.dirname(__file__)))
ico_path=os.path.abspath(os.path.dirname(__file__))



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #创建提示框（10size大小的SansSerif字体）
        QToolTip.setFont(QFont('SansSerif',10))
        #静态方法设置字体，使用富文本格式的内容
        self.setToolTip('This is a <b>QWidget</b> widget')

        #创建一个按钮
        btn = QPushButton('button',self)
        #并为按钮创建一个提示框
        btn.setToolTip('This is a <b>QPushButton</b> widget') 
        btn.resize(btn.sizeHint())#默认大小的按钮
        #按钮位置（相对于窗口空白位置）
        btn.move(0,0)

        #创建一个关闭按钮
        qbth = QPushButton('quit',self)
        '''
        信号机制，QCoreApplication包含事件的主循环 
        instance创建的实例,点击事件和quit函数绑定在一起
        '''
        qbth.clicked.connect(QCoreApplication.instance().quit)
        qbth.resize(qbth.sizeHint())
        qbth.move(100,0)#绝对位置

        self.resize(300,300)
        self.center()
        self.setWindowTitle('批量上传')
        self.setWindowIcon(QIcon(ico_path+'/upload.ico'))
        
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'message','是否关闭',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        '''
        窗口居中
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    apps=QApplication(sys.argv)
    ex=Example()
    sys.exit(apps.exec_())
