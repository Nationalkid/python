import sys
from PyQt5.QtWidgets import  QApplication
from Qt.MainWindow import MainWindow
#from Qt.CreateTable import CreateTable

if __name__ == '__main__':
    qtApp = QApplication(sys.argv)
    #tbl = CreateTable()
    lk = MainWindow()
    lk.run()
    sys.exit(qtApp.exec_())
