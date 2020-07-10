# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import os
import sys


from qrc import qrc



ico_path=os.path.abspath(os.path.dirname(__file__))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 877)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        '''
        整体栅格布局，自适应界面
        '''
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        '''
        信息打印，脚本输入区域
        '''
        self.tabWidget_print = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_print.setMinimumSize(QtCore.QSize(871, 193))
        self.tabWidget_print.setMaximumSize(QtCore.QSize(1920, 1080))
        self.tabWidget_print.setObjectName("tabWidget_print")

        '''
        脚本信息输入，打印
        '''
        self.tab_JB_pr = QtWidgets.QWidget()
        self.tab_JB_pr.setStatusTip("")
        self.tab_JB_pr.setObjectName("tab_JB_pr")

        '''
        TextEdit输入框和TabWidget栅格布局，使其自适应窗口
        '''
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_JB_pr)
        self.gridLayout_8.setObjectName("gridLayout_8")
       
        self.textEdit = QtWidgets.QTextEdit(self.tab_JB_pr)
        self.textEdit.setMinimumSize(QtCore.QSize(857, 193))
        self.textEdit.setMaximumSize(QtCore.QSize(1920, 1080))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_8.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget_print.addTab(self.tab_JB_pr, "")

        '''
        数据库脚本信息打印输入
        '''
        self.tab_DB_SQL = QtWidgets.QWidget()
        self.tab_DB_SQL.setObjectName("tab_DB_SQL")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_DB_SQL)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.textEdit_DBSQL = QtWidgets.QTextEdit(self.tab_DB_SQL)
        self.textEdit_DBSQL.setMinimumSize(QtCore.QSize(857, 193))
        self.textEdit_DBSQL.setMaximumSize(QtCore.QSize(1920, 1080))
        self.textEdit_DBSQL.setObjectName("textEdit_DBSQL")
        self.gridLayout_9.addWidget(self.textEdit_DBSQL, 0, 0, 1, 1)
        self.tabWidget_print.addTab(self.tab_DB_SQL, "")
        
        '''
        异常报错打印，日志
        '''
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName("gridLayout_10")

        self.textEdit_error = QtWidgets.QTextEdit(self.tab)
        self.textEdit_error.setMinimumSize(QtCore.QSize(857, 193))
        self.textEdit_error.setMaximumSize(QtCore.QSize(1920, 1080))
        self.textEdit_error.setObjectName("textEdit_error")

        self.gridLayout_10.addWidget(self.textEdit_error, 0, 0, 1, 1)

        self.tabWidget_print.addTab(self.tab, "")


        self.gridLayout_4.addWidget(self.tabWidget_print, 2, 0, 1, 1)#全局栅格布局下方位置

        '''
        右侧框区域
        '''
        self.tabWidget_right = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_right.setMinimumSize(QtCore.QSize(200, 580))
        self.tabWidget_right.setMaximumSize(QtCore.QSize(200, 580))
        self.tabWidget_right.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget_right.setObjectName("tabWidget_right")

        '''
        数据库连接区域
        '''
        self.tab_DB = QtWidgets.QWidget()
        self.tab_DB.setObjectName("tab_DB")
        self.line = QtWidgets.QFrame(self.tab_DB)
        self.line.setGeometry(QtCore.QRect(0, 230, 201, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line.setObjectName("line")

        '''
        数据库表显示，连接后显示
        '''
        self.tabWidget_two = QtWidgets.QTabWidget(self.tab_DB)
        self.tabWidget_two.setGeometry(QtCore.QRect(-1, 250, 201, 307))
        self.tabWidget_two.setObjectName("tabWidget_two")

        self.tab_table = QtWidgets.QWidget()
        self.tab_table.setObjectName("tab_table")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_table)
        self.treeWidget.setGeometry(QtCore.QRect(-2, -1, 201, 286))#位置大小参数
        self.treeWidget.setObjectName("treeWidget") #所有表显示区域
        self.treeWidget.headerItem().setText(0, "表1")
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(205, 170, 222))
        self.tabWidget_two.addTab(self.tab_table, "")
        
        '''
        数据库连接信息区域
        '''
        self.tab_site = QtWidgets.QWidget()
        self.tab_site.setObjectName("tab_site")
        self.tabWidget_two.addTab(self.tab_site, "")

        self.layoutWidget = QtWidgets.QWidget(self.tab_DB)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 12, 191, 211))
        self.layoutWidget.setObjectName("layoutWidget")

        self.gridLayout_DB_input = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_DB_input.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_DB_input.setObjectName("gridLayout_DB_input")
        
        '''
        栅格布局
        '''
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        '''
        水平布局，输入框标签
        '''
        self.verticalLayout_tags = QtWidgets.QVBoxLayout()
        self.verticalLayout_tags.setObjectName("verticalLayout_tags")

        self.label_user = QtWidgets.QLabel(self.layoutWidget)#用户名
        self.label_user.setObjectName("label_user")
        self.verticalLayout_tags.addWidget(self.label_user)

        self.label_pwd = QtWidgets.QLabel(self.layoutWidget)#密码
        self.label_pwd.setObjectName("label_pwd")
        self.verticalLayout_tags.addWidget(self.label_pwd)

        self.label_IP = QtWidgets.QLabel(self.layoutWidget)#IP地址
        self.label_IP.setObjectName("label_IP")
        self.verticalLayout_tags.addWidget(self.label_IP)

        self.label_port = QtWidgets.QLabel(self.layoutWidget)#端口
        self.label_port.setObjectName("label_port")
        self.verticalLayout_tags.addWidget(self.label_port)

        '''
        栅格布局标签区域
        '''
        self.gridLayout.addLayout(self.verticalLayout_tags, 0, 0, 1, 1)

        '''
        水平布局，输入框
        '''
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit_user = QtWidgets.QLineEdit(self.layoutWidget)#用户名
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout.addWidget(self.lineEdit_user)

        self.lineEdit_passw = QtWidgets.QLineEdit(self.layoutWidget)#密码
        self.lineEdit_passw.setObjectName("lineEdit_passw")
        self.verticalLayout.addWidget(self.lineEdit_passw)

        self.lineEdit_IP = QtWidgets.QLineEdit(self.layoutWidget)#IP地址
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.verticalLayout.addWidget(self.lineEdit_IP)

        self.lineEdit_port = QtWidgets.QLineEdit(self.layoutWidget)#端口
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        '''
        栅格布局输入框区域
        '''
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_DB_input.addLayout(self.gridLayout, 0, 0, 1, 2)

        '''
        按钮
        '''
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_DB_input.addWidget(self.checkBox, 1, 0, 1, 1)#栅格布局选择记住密码按钮

        self.pushButton_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.gridLayout_DB_input.addWidget(self.pushButton_ok, 2, 0, 1, 1)#栅格布局确认按钮

        self.pushButton_dis = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_dis.setObjectName("pushButton_dis")
        self.gridLayout_DB_input.addWidget(self.pushButton_dis, 2, 1, 1, 1)#栅格布局断开连接按钮

        self.tabWidget_right.addTab(self.tab_DB, "")

        '''
        右侧远程连接SSH配置
        '''
        self.tab_SSH = QtWidgets.QWidget()
        self.tab_SSH.setObjectName("tab_SSH")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_SSH)
        self.layoutWidget1.setGeometry(QtCore.QRect(-2, 8, 201, 211))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_SSH_INPUT = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_SSH_INPUT.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_SSH_INPUT.setObjectName("gridLayout_SSH_INPUT")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_tags_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tags_2.setObjectName("verticalLayout_tags_2")
        self.label_user_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_user_2.setObjectName("label_user_2")
        self.verticalLayout_tags_2.addWidget(self.label_user_2)
        self.label_pwd_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_pwd_2.setObjectName("label_pwd_2")
        self.verticalLayout_tags_2.addWidget(self.label_pwd_2)
        self.label_host_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_host_2.setObjectName("label_host_2")
        self.verticalLayout_tags_2.addWidget(self.label_host_2)
        self.label_port_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_port_2.setObjectName("label_port_2")
        self.verticalLayout_tags_2.addWidget(self.label_port_2)
        self.gridLayout_3.addLayout(self.verticalLayout_tags_2, 0, 0, 1, 1)
        self.gridLayout_SSH_INPUT_2 = QtWidgets.QGridLayout()
        self.gridLayout_SSH_INPUT_2.setObjectName("gridLayout_SSH_INPUT_2")
        self.lineEdit_user_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_user_2.setMaximumSize(QtCore.QSize(153, 20))
        self.lineEdit_user_2.setObjectName("lineEdit_user_2")
        self.gridLayout_SSH_INPUT_2.addWidget(self.lineEdit_user_2, 0, 0, 1, 1)
        self.lineEdit_passw_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_passw_2.setMaximumSize(QtCore.QSize(153, 20))
        self.lineEdit_passw_2.setObjectName("lineEdit_passw_2")
        self.gridLayout_SSH_INPUT_2.addWidget(self.lineEdit_passw_2, 1, 0, 1, 1)
        self.lineEdit_IP_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_IP_2.setMaximumSize(QtCore.QSize(153, 20))
        self.lineEdit_IP_2.setObjectName("lineEdit_IP_2")
        self.gridLayout_SSH_INPUT_2.addWidget(self.lineEdit_IP_2, 2, 0, 1, 1)
        self.lineEdit_port_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_port_2.setMinimumSize(QtCore.QSize(153, 20))
        self.lineEdit_port_2.setMaximumSize(QtCore.QSize(153, 20))
        self.lineEdit_port_2.setObjectName("lineEdit_port_2")
        self.gridLayout_SSH_INPUT_2.addWidget(self.lineEdit_port_2, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_SSH_INPUT_2, 0, 1, 1, 1)
        self.gridLayout_SSH_INPUT.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_SSH_INPUT.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_SSH_INPUT.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_SSH_INPUT.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.tabWidget_right.addTab(self.tab_SSH, "")

        '''
        右侧人脸设置
        '''
        self.tab_Face = QtWidgets.QWidget()
        self.tab_Face.setObjectName("tab_Face")
        self.tabWidget_right.addTab(self.tab_Face, "")

        self.gridLayout_4.addWidget(self.tabWidget_right, 0, 1, 1, 1)#全局栅格布局，右侧位置


        '''
        左侧Tab区域，(数据库表详细数据，Excel打开文件读取数据，图片选择数据，SSH远程连接)
        '''
        self.tabWidget_left = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_left.setMinimumSize(QtCore.QSize(871, 548))
        self.tabWidget_left.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_left.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget_left.setObjectName("tabWidget_left")

        '''
        左侧 数据库表数据
        '''
        self.tab_left_DB = QtWidgets.QWidget()
        self.tab_left_DB.setObjectName("tab_left_DB")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_left_DB)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_left_db = QtWidgets.QTableWidget(self.tab_left_DB)
        self.tableWidget_left_db.setMinimumSize(QtCore.QSize(857, 548))
        self.tableWidget_left_db.setRowCount(500)
        self.tableWidget_left_db.setColumnCount(500)
        self.tableWidget_left_db.setObjectName("tableWidget_left_db")
        self.gridLayout_2.addWidget(self.tableWidget_left_db, 0, 0, 1, 1)
        self.gridLayout_2.setSpacing(1)
        self.tabWidget_left.addTab(self.tab_left_DB, "")

        '''
        左侧 excel批量上传数据库数据信息
        '''
        self.tab_left_Excel = QtWidgets.QWidget()
        self.tab_left_Excel.setObjectName("tab_left_Excel")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_left_Excel)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_left_Excel = QtWidgets.QTableWidget(self.tab_left_Excel)
        self.tableWidget_left_Excel.setMinimumSize(QtCore.QSize(857, 548))
        self.tableWidget_left_Excel.setMaximumSize(QtCore.QSize(1920, 1080))
        self.tableWidget_left_Excel.setRowCount(500)
        self.tableWidget_left_Excel.setColumnCount(500)
        self.tableWidget_left_Excel.setObjectName("tableWidget_left_Excel")
        self.gridLayout_5.addWidget(self.tableWidget_left_Excel, 0, 0, 1, 1)
        self.tabWidget_left.addTab(self.tab_left_Excel, "")

        '''
        左侧 人脸图片，以及数据
        '''
        self.tab_left_Face = QtWidgets.QWidget()
        self.tab_left_Face.setObjectName("tab_left_Face")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_left_Face)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.tab_left_Face)
        self.treeWidget_2.setMinimumSize(QtCore.QSize(857, 548))
        self.treeWidget_2.setMaximumSize(QtCore.QSize(1920, 1080))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "图片显示")
        self.gridLayout_6.addWidget(self.treeWidget_2, 0, 0, 1, 1)
        self.tabWidget_left.addTab(self.tab_left_Face, "")
        
        '''
        左侧 SSH远程连接文件目录选择
        '''
        self.tab_left_SSHFile = QtWidgets.QWidget()
        self.tab_left_SSHFile.setObjectName("tab_left_SSHFile")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_left_SSHFile)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.treeWidget_left_File = QtWidgets.QTreeWidget(self.tab_left_SSHFile)
        self.treeWidget_left_File.setMinimumSize(QtCore.QSize(857, 548))
        self.treeWidget_left_File.setMaximumSize(QtCore.QSize(1920, 1080))
        self.treeWidget_left_File.setObjectName("treeWidget_left_File")

        self.gridLayout_7.addWidget(self.treeWidget_left_File, 0, 0, 1, 1)
        self.tabWidget_left.addTab(self.tab_left_SSHFile, "")

        self.gridLayout_4.addWidget(self.tabWidget_left, 0, 0, 1, 1)#全局栅格布局左侧位置

        '''
        mainwindow主界面添加centralwidget区域
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        
        #菜单栏
        self.menuBar = QtWidgets.QMenuBar(MainWindow)

        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1095, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_edit = QtWidgets.QMenu(self.menuBar)
        self.menu_edit.setObjectName("menu_edit")
        self.menuExcel = QtWidgets.QMenu(self.menuBar)
        self.menuExcel.setObjectName("menuExcel")
        self.menu_db = QtWidgets.QMenu(self.menuBar)
        self.menu_db.setObjectName("menu_db")
        self.menu_rem = QtWidgets.QMenu(self.menuBar)
        self.menu_rem.setObjectName("menu_rem")
        self.menu_128 = QtWidgets.QMenu(self.menuBar)
        self.menu_128.setObjectName("menu_128")
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")

        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")

        '''
        mainwindow主界面添加菜单栏区域
        '''
        MainWindow.setMenuBar(self.menuBar)

        '''
        工具栏区域
        '''
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        '''
        菜单栏区域
        '''
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        #ico图标设置
        self.actionnew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":zes/文件图标1/Ab1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew.setIcon(icon)
        self.actionnew.setIconText("文件")
        self.actionnew.setStatusTip("")
        self.actionnew.setWhatsThis("")
        self.actionnew.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":002/文件图标1/Cdd12.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon1)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setIcon(icon1)
        self.actionsave.setObjectName("actionsave")
        self.actionaotu_save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":002/文件图标1/Cdd16.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionaotu_save.setIcon(icon2)
        self.actionaotu_save.setObjectName("actionaotu_save")
        self.actionquit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":002/文件图标1/Cdd4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionquit.setIcon(icon3)
        self.actionquit.setObjectName("actionquit")
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actionrestore = QtWidgets.QAction(MainWindow)
        self.actionrestore.setObjectName("actionrestore")
        self.actioncut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":002/文件图标1/001.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncut.setIcon(icon4)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":002/文件图标1/002.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncopy.setIcon(icon5)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":002/文件图标1/003.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpaste.setIcon(icon6)
        self.actionpaste.setObjectName("actionpaste")
        self.actionfind = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":other/文件图标1/Aw19.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfind.setIcon(icon7)
        self.actionfind.setObjectName("actionfind")
        self.actionreplace = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":006/文件图标1/系统电脑桌面图标下载0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionreplace.setIcon(icon8)
        self.actionreplace.setObjectName("actionreplace")
        self.actionnewe = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":文件扩展/文件图标1/Dh20.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnewe.setIcon(icon9)
        self.actionnewe.setObjectName("actionnewe")
        self.actionopene = QtWidgets.QAction(MainWindow)
        self.actionopene.setObjectName("actionopene")
        self.actionconnect = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":003/文件图标1/j8.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionconnect.setIcon(icon10)
        self.actionconnect.setObjectName("actionconnect")
        self.actiondisconnect = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":003/文件图标1/j7.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondisconnect.setIcon(icon11)
        self.actiondisconnect.setObjectName("actiondisconnect")
        self.actionhang = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":003/文件图标1/j1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionhang.setIcon(icon12)
        self.actionhang.setObjectName("actionhang")
        self.actiondbsite = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":文件扩展1/文件图标1/f6.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondbsite.setIcon(icon13)
        self.actiondbsite.setObjectName("actiondbsite")
        self.actionpannel = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":文件扩展1/文件图标1/f8.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionpannel.setIcon(icon14)
        self.actionpannel.setObjectName("actionpannel")
        self.actionInterrupt = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":003/文件图标1/j30.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInterrupt.setIcon(icon15)
        self.actionInterrupt.setObjectName("actionInterrupt")
        self.actionCconnect = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":003/文件图标1/j3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCconnect.setIcon(icon16)
        self.actionCconnect.setObjectName("actionCconnect")
        self.actionDisCconnect = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":003/文件图标1/j25.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisCconnect.setIcon(icon17)
        self.actionDisCconnect.setObjectName("actionDisCconnect")
        self.actionfacephoto = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":文件扩展/文件图标1/Dh9.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfacephoto.setIcon(icon18)
        self.actionfacephoto.setObjectName("actionfacephoto")
        self.actionfacesite = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":006/文件图标1/系统电脑桌面图标下载1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfacesite.setIcon(icon19)
        self.actionfacesite.setObjectName("actionfacesite")
        self.actionBatchcollect = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":005/文件图标1/Ai2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBatchcollect.setIcon(icon20)
        self.actionBatchcollect.setObjectName("actionBatchcollect")
        self.actionabout = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":006/文件图标1/系统电脑桌面图标下载3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout.setIcon(icon21)
        self.actionabout.setObjectName("actionabout")
        self.actionsearch = QtWidgets.QAction(MainWindow)
        self.actionsearch.setIcon(icon7)
        self.actionsearch.setObjectName("actionsearch")
        self.menu_edit.addAction(self.actionundo)
        self.menu_edit.addAction(self.actionrestore)
        self.menu_edit.addAction(self.actioncut)
        self.menu_edit.addAction(self.actioncopy)
        self.menu_edit.addAction(self.actionpaste)
        self.menu_edit.addAction(self.actionfind)
        self.menu_edit.addAction(self.actionreplace)
        self.menuExcel.addAction(self.actionnewe)
        self.menuExcel.addAction(self.actionopene)
        self.menu_db.addAction(self.actionconnect)
        self.menu_db.addAction(self.actiondisconnect)
        self.menu_db.addAction(self.actionhang)
        self.menu_db.addAction(self.actiondbsite)
        self.menu_rem.addAction(self.actionpannel)
        self.menu_rem.addAction(self.actionInterrupt)
        self.menu_rem.addAction(self.actionCconnect)
        self.menu_rem.addAction(self.actionDisCconnect)
        self.menu_128.addAction(self.actionfacephoto)
        self.menu_128.addAction(self.actionfacesite)
        self.menu_128.addAction(self.actionBatchcollect)
        self.menu_file.addAction(self.actionnew)
        self.menu_file.addAction(self.actionopen)
        self.menu_file.addAction(self.actionsave)
        self.menu_file.addAction(self.actionaotu_save)
        self.menu_file.addAction(self.actionquit)
        self.menu.addAction(self.actionabout)
        self.menu.addAction(self.actionsearch)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_edit.menuAction())
        self.menuBar.addAction(self.menuExcel.menuAction())
        self.menuBar.addAction(self.menu_db.menuAction())
        self.menuBar.addAction(self.menu_rem.menuAction())
        self.menuBar.addAction(self.menu_128.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addAction(self.actionfind)
        self.toolBar.addAction(self.actionnewe)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionconnect)
        self.toolBar.addAction(self.actiondisconnect)
        self.toolBar.addAction(self.actionhang)
        self.toolBar.addAction(self.actiondbsite)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionfacephoto)
        self.toolBar.addAction(self.actionBatchcollect)
        self.toolBar.addAction(self.actionfacesite)
        self.toolBar.addAction(self.actionpannel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionsearch)

        self.retranslateUi(MainWindow)
        self.tabWidget_print.setCurrentIndex(2)
        self.tabWidget_right.setCurrentIndex(0)
        self.tabWidget_two.setCurrentIndex(0)
        self.tabWidget_left.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "批量上传"))
        self.tabWidget_print.setTabText(self.tabWidget_print.indexOf(self.tab_JB_pr), _translate("MainWindow", "python脚本"))
        self.tabWidget_print.setTabText(self.tabWidget_print.indexOf(self.tab_DB_SQL), _translate("MainWindow", "数据库脚本"))
        self.tabWidget_print.setTabText(self.tabWidget_print.indexOf(self.tab), _translate("MainWindow", "异常报错"))
        self.tabWidget_two.setTabText(self.tabWidget_two.indexOf(self.tab_table), _translate("MainWindow", "数据库表"))
        self.tabWidget_two.setTabText(self.tabWidget_two.indexOf(self.tab_site), _translate("MainWindow", "配置"))
        self.label_user.setText(_translate("MainWindow", "用户"))
        self.label_pwd.setText(_translate("MainWindow", "密码"))
        self.label_IP.setText(_translate("MainWindow", "IP"))
        self.label_port.setText(_translate("MainWindow", "端口"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_ok.setText(_translate("MainWindow", "确认连接"))
        self.pushButton_dis.setText(_translate("MainWindow", "断开"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_DB), _translate("MainWindow", "数据库"))
        self.label_user_2.setText(_translate("MainWindow", "用户"))
        self.label_pwd_2.setText(_translate("MainWindow", "密码"))
        self.label_host_2.setText(_translate("MainWindow", "host"))
        self.label_port_2.setText(_translate("MainWindow", "端口"))
        self.checkBox_2.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_4.setText(_translate("MainWindow", "确认连接"))
        self.pushButton_3.setText(_translate("MainWindow", "断开"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_SSH), _translate("MainWindow", "远程SSH"))
        self.tabWidget_right.setTabText(self.tabWidget_right.indexOf(self.tab_Face), _translate("MainWindow", "人脸"))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_left_DB), _translate("MainWindow", "DB"))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_left_Excel), _translate("MainWindow", "EXCEL"))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_left_Face), _translate("MainWindow", "photo"))
        self.treeWidget_left_File.headerItem().setText(0, _translate("MainWindow", "系统文件"))
        self.tabWidget_left.setTabText(self.tabWidget_left.indexOf(self.tab_left_SSHFile), _translate("MainWindow", "SSHFile"))
        self.menu_edit.setTitle(_translate("MainWindow", "编辑"))
        self.menuExcel.setTitle(_translate("MainWindow", "Excel"))
        self.menu_db.setTitle(_translate("MainWindow", "数据库"))
        self.menu_rem.setTitle(_translate("MainWindow", "远程连接"))
        self.menu_128.setTitle(_translate("MainWindow", "人脸128"))
        self.menu_file.setWhatsThis(_translate("MainWindow", "打开"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionnew.setToolTip(_translate("MainWindow", "新建文件"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionopen.setText(_translate("MainWindow", "打开文件"))
        self.actionsave.setText(_translate("MainWindow", "保存"))
        self.actionaotu_save.setText(_translate("MainWindow", "自动保存"))
        self.actionquit.setText(_translate("MainWindow", "退出"))
        self.actionundo.setText(_translate("MainWindow", "撤销"))
        self.actionrestore.setText(_translate("MainWindow", "恢复"))
        self.actioncut.setText(_translate("MainWindow", "剪切"))
        self.actioncut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actioncopy.setText(_translate("MainWindow", "复制"))
        self.actioncopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionpaste.setText(_translate("MainWindow", "粘贴"))
        self.actionpaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionfind.setText(_translate("MainWindow", "查找"))
        self.actionreplace.setText(_translate("MainWindow", "替换"))
        self.actionnewe.setText(_translate("MainWindow", "新建Excel"))
        self.actionopene.setText(_translate("MainWindow", "打开"))
        self.actionconnect.setText(_translate("MainWindow", "连接"))
        self.actiondisconnect.setText(_translate("MainWindow", "断开"))
        self.actionhang.setText(_translate("MainWindow", "挂起"))
        self.actiondbsite.setText(_translate("MainWindow", "设置"))
        self.actionpannel.setText(_translate("MainWindow", "控制面板"))
        self.actionInterrupt.setText(_translate("MainWindow", "中断"))
        self.actionCconnect.setText(_translate("MainWindow", "集群连接"))
        self.actionDisCconnect.setText(_translate("MainWindow", "集群中断"))
        self.actionfacephoto.setText(_translate("MainWindow", "图片"))
        self.actionfacesite.setText(_translate("MainWindow", "人脸设置"))
        self.actionBatchcollect.setText(_translate("MainWindow", "批量采集"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionsearch.setText(_translate("MainWindow", "搜索"))



if __name__ == '__main__':
    gus=QApplication(sys.argv)

    MainWindow=QMainWindow()  

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(gus.exec_())
