import sys
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton,\
    QDesktopWidget, QInputDialog, QFileDialog, QComboBox, \
    QVBoxLayout,QHBoxLayout, QFormLayout, QStatusBar, QMainWindow

from PyQt5.QtCore import QFileInfo,qDebug,QObject,pyqtSignal
from Qt.CreateTable import CreateTable
from xlrd import open_workbook

# Class definition
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 400, 600, 400)
        self.setWindowTitle('Antonio\'s likert scale bar plot generator')
        self.center()
        self.land_use = ['agriculture', 'forest', 'settlement', 'grassland']
        self.services = ['food', 'wood', 'water_supply', 'regulation', 'air_quality', 'scenic_beauty']

        # Defining combo boxes
        cmbServices = QComboBox()
        cmbLandScape = QComboBox()
        cmbServices.addItems(self.services)
        cmbLandScape.addItems(self.land_use)
        cmbServices.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        cmbLandScape.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)

        # Defining labels:
        lblServices = QLabel('Select a service')
        lblLandScape = QLabel('Select a land scape')

        # Button definition
        btnOpen = QPushButton('Open', self)
        btnQuit = QPushButton('Quit', self)
        btnTest = QPushButton('Test', self)
        #table = CreateTable()
        btnOpen.setStatusTip('Open the excel File')
        btnOpen.clicked.connect(self.showOpenFileDialog)
        #btnOpen.clicked.connect(self.showTable)
        btnQuit.clicked.connect(self.quitApp)
        #btnTest.clicked.connect(self.showTable)

        # Defining table widget
        # Form layout for combos and labels
        self.combosLayout = QVBoxLayout()
        self.combosLayout.addWidget(lblServices)
        self.combosLayout.addWidget(cmbServices)
        self.combosLayout.addWidget(lblLandScape)
        self.combosLayout.addWidget(cmbLandScape)

        #Horizontal layout for buttons
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(btnOpen)
        self.buttonsLayout.addWidget(btnQuit)
        self.buttonsLayout.addWidget(btnTest)
        self.buttonsLayout.addStretch()

        #Setting some space and putting layouts together
        self.mainLayout = QFormLayout()
        self.mainLayout.setContentsMargins(20, 20, 150, 150)
        self.mainLayout.addRow(self.combosLayout)
        self.mainLayout.addRow(self.buttonsLayout)

        # Creating a widget (for cental widget) and set the layout for the window
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.central_widget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr  .moveCenter(cp)
        self.move(qr.topLeft())

    def showOpenFileDialog(self):
        #For static function call
        filename = QFileDialog.getOpenFileName(self, 'Open file',
         'c:\\Users\\Elena Arsevska\\Dropbox\\R\\',"Excel files (*.xls *.xlsx)")
        filepath = filename[0]
        print(filepath)
        if filename:
            file = open(filepath, 'r')
            print("Filename  : " + filepath)
            self.statusBar().showMessage("Loaded file : " + filepath)
            workbook = open_workbook(filepath)
            '''
            for sheet in workbook.sheets():
                print('Sheet:' + sheet.name)
                values = []
                for row in range(sheet.nrows):
                    col_value = []
                    for col in range(sheet.ncols):
                        value = sheet.cell(row, col).value
                        try:
                            value = str(int(value))
                        except:
                            pass
                        col_value.append(value)
                        values.append(col_value)
            print (values)
            '''
        self.showTable(workbook)

    def showTable(self, workbook):
        self.table = CreateTable()
        self.table.fillTable(workbook)
        self.table.centerTable()
        self.table.show()


    # Only the active windows closes, not the whole program
    def quitApp(self):
        self.close()

    def run(self):
        self.show()
# Only the active windows closes, not the whole program


