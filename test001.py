import sys
from PyQt5.QtWidgets import QApplication,QWidget



if __name__ == '__main__':
    #应用对象
    app = QApplication(sys.argv)
    w = QWidget()
    #窗口大小
    w.resize(320,180)
     #窗口对于屏幕坐标的位置
    w.move(300,300)
    #窗口标题
    w.setWindowTitle("测试")
    w.show()

    sys.exit(app.exec_())