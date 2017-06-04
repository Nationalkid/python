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
        cmbServices.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        cmbLandScape.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        # Defining labels:
        lblServices = QLabel('Select a service')
        lblLandScape = QLabel('Select a land scape')

        # Button definition
        self.btnOpen = QPushButton('Open', self)
        self.btnQuit = QPushButton('Quit', self)
        self.btnRun = QPushButton('Run', self)
        self.btnRun.setDisabled(True)

        # Connecting slots
        self.btnOpen.setStatusTip('Open the excel File')
        self.btnOpen.clicked.connect(self.showOpenFileDialog)
        self.btnQuit.clicked.connect(self.quitApp)

        # Defining table widget
        # Form layout for combos and labels
        self.combosLayout = QVBoxLayout()
        self.combosLayout.addWidget(lblServices)
        self.combosLayout.addWidget(cmbServices)
        self.combosLayout.addWidget(lblLandScape)
        self.combosLayout.addWidget(cmbLandScape)
        self.combosLayout.addStretch()

        #Horizontal layout for buttons
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(self.btnOpen)
        self.buttonsLayout.addWidget(self.btnQuit)
        self.buttonsLayout.addWidget(self.btnRun)
        self.buttonsLayout.addStretch()

        #Setting some space and putting layouts together
        self.mainLayout = QFormLayout()
        self.mainLayout.setContentsMargins(20, 20, 250, 150)
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
        #fileDialog = QFileDialog()
        filename = QFileDialog.getOpenFileName(None, 'Open file',
         'c:\\Users\\Elena Arsevska\\Dropbox\\R\\',"Excel files (*.xls *.xlsx)")
        if filename[0]:
            filepath = filename[0]
            file = open(filepath, 'r')
            print("Filename  : " + filepath)
            self.statusBar().showMessage("Loaded file : " + filepath)
            workbook = open_workbook(filepath)
            self.showTable(workbook)
            self.btnRun.setEnabled(True)
        if not filename[0]:
            print("empty")
            self.statusBar().showMessage("Ready")



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


