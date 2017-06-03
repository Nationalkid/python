from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QDesktopWidget
# from PyQt5.QtCore import pyqtSlot,QFile,QFileInfo
from xlrd import open_workbook


class CreateTable(QTableWidget):

    def __init__(self):

        super().__init__()

        # Create a tableWidget
        # self.tableWidget = QTableWidget()
        # Create a QVBoxLayout layout and add the object's table widget to it.
        # self.layoutVBox = QVBoxLayout()
        # self.layoutVBox.addWidget(self.tableWidget)
        # Set objects' layout
        # self.setLayout(self.layoutVBox)
        # Fill, Center and show widget
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Table view")
        #self.setGeometry(30, 30, 500, 500)
        self.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        #self.fillTable()
        #self.center()
        #self.show()

    def fillTable(self, workbook):

        # print(fileName)
        # with fileName:
        #    data = filename.read()
        #    # skip these lines if you don't have headers
        #    headers = data[0]
        #    data = data[1:]
        #    self.sethorizontalheaderlabels(headers)

        # Fill table
        '''
        self.setRowCount(4)
        self.setColumnCount(2)
        self.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        '''
        for sheet in workbook.sheets():
            print('Sheet:' + sheet.name)
            self.setRowCount(sheet.nrows)
            self.setColumnCount(sheet.ncols)
            #self.removeRow(0)
            # headers = [str(cell.value) for cell in sheet.row(0)]
            # print(headers)
            # self.setHorizontalHeaderLabels(headers)
            print(sheet.nrows)
            for col in range(sheet.ncols):
                colLabel = sheet.cell(0, col).value
                print(colLabel)
                self.setHorizontalHeaderItem(col, QTableWidgetItem(colLabel))
                #Start from line 1
                for row in range(1, sheet.nrows):
                    value = sheet.cell(row, col).value
                    self.setItem(row - 1, col, QTableWidgetItem(value))
                    try:
                        value = str(int(value))
                    except:
                        pass
                    #col_value.append(value)
                    #values.append(col_value)
        #print(values)

    def centerTable(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr  .moveCenter(cp)
        self.move(qr.topLeft())


    # for row, columnvalues in enumerate(data):
    #    for column, value in enumerate(columnvalues):
    #        item = QtGui.QTableWidgetItem(value)
    #        mytable.setItem(row, column, item)