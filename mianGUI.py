import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp,QMenu,QTextEdit
from PyQt5.QtGui import QIcon
import os


ico_path=os.path.abspath(os.path.dirname(__file__))



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        '''
        文件菜单栏
        '''
        #Icon图标
        exitAct = QAction(QIcon(ico_path+'/upload.ico'),'&exit',self)
        exitAct.setShortcut('Ctrl+Q')   #菜单栏命令
        exitAct.setStatusTip('退出应用')    #状态栏，当鼠标悬停菜单栏时，显示当前状态
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件') #创建菜单栏
        fileMenu.addAction(exitAct) #添加

        impMenu = QMenu('import',self)  #二级菜单
        impAct = QAction('import main',self) #三级菜单
        impMenu.addAction(impAct)  #三级菜单添加到二级菜单，addAction添加动作

        newAct = QAction('new',self)    #二级菜单

        fileMenu.addAction(newAct)  #菜单绑定
        fileMenu.addMenu(impMenu)   #菜单绑定到菜单


        '''
        #视图菜单，状态栏
        '''
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')


        menubar1 = self.menuBar()
        viewMenu = menubar1.addMenu('视图')

        viewStatAct = QAction('view',self,checkable=True)   #checkable创建一个能选中的菜单
        viewStatAct.setStatusTip('view')    #状态栏
        viewStatAct.setChecked(True) #默认设置为选中状态
        viewStatAct.triggered.connect(self.toggleMenu)  #事件和动作连接在一起，用信号

        viewMenu.addAction(viewStatAct) #将上述添加到视图菜单
        #状态栏
        # self.statusBar().showMessage('状态栏')    

        '''
        工具栏
        '''
        playAct = QAction(QIcon(ico_path+'/7735/Av1.ico'),'播放',self)
        playAct.setShortcut('Ctrl+F')
        playAct.triggered.connect(qApp.quit)

        self.playbar = self.addToolBar('播放')
        self.playbar.addAction(playAct)

        '''
        文本区域
        '''
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        '''
        窗口设置
        '''
        self.setGeometry(300,300,350,250)
        self.setWindowTitle('test')
        self.show()

    def contextMenuEvent(self,event):
        '''
        右键菜单
        '''
        cmenu = QMenu(self)

        newAct = cmenu.addAction('新建')
        FFAct = cmenu.addAction('刷新')
        quitAct = cmenu.addAction('退出')

        '''
        exec_显示菜单 从鼠标右键事件对象中获得当前坐标。
        mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        '''
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def toggleMenu(self,state):
        '''
        根据选中状态判断是否显示
        '''
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__=='__main__':
    gu=QApplication(sys.argv)
    sd=Example()
    sys.exit(gu.exec_())