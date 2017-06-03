from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout,QDesktopWidget,QTableView
from PyQt5.QtCore import pyqtSlot,QFile,QFileInfo


class CreateTable(QTableWidget):
    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.title = 'Table'
        self.left = 30
        self.top = 100
        self.width = 300
        self.height = 200
        #self.initUI()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Create table. Must be donne before layout
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.resizeColumnsToContents()
        self.setLayout(self.layout)
        # Center and show widget
        self.center()
        self.show()

    def createTable(self):

        #print(fileName)
        #with fileName:
        #    data = filename.read()
        #    # skip these lines if you don't have headers
        #    headers = data[0]
        #    data = data[1:]
        #    self.sethorizontalheaderlabels(headers)

        #for row, columnvalues in enumerate(data):
        # for column, value in enumerate(columnvalues):
        #        item = QtGui.QTableWidgetItem(value)
        #        mytable.setItem(row, column, item)


        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setFixedSize(self.tableWidget.sizeHint())


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr  .moveCenter(cp)
        self.move(qr.topLeft())

    #for row, columnvalues in enumerate(data):
    #    for column, value in enumerate(columnvalues):
    #        item = QtGui.QTableWidgetItem(value)
    #        mytable.setItem(row, column, item)