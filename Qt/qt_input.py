import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel,\
    QDesktopWidget, QInputDialog,QFileDialog,QMainWindow,QTextEdit,QAction,QComboBox,\
    QSizePolicy,QVBoxLayout,QFormLayout,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class LeikertWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #Adding a new QWidget
        # Main window options
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('File dialog')
         # self.statusBar()
        #self.setWindowTitle('Dynamic Greeter')
        #self.setMinimumWidth(400)

        self.land_use = ['agriculture', 'forest', 'settlement', 'grassland']
        self.services = ['food', 'wood', 'water_supply', 'regulation', 'air_quality', 'scenic_beauty']

        #Defining combo boxes
        cmbServices = QComboBox()
        cmbLandScape = QComboBox()
        cmbServices.addItems(self.services)
        cmbLandScape.addItems(self.land_use)
        cmbServices.AdjustToMinimumContentsLength
        cmbLandScape.AdjustToMinimumContentsLength

        #Defining labels:
        lblServices = QLabel('Select a service')
        lblLandScape = QLabel('Select a land scape')

        #Button definition
        btnOpen = QPushButton('Open', self)
        btnQuit = QPushButton('Quit', self)
        btnOpen.setStatusTip('Open the excel File')
        btnOpen.clicked.connect(self.showOpenFileDialog)
        btnQuit.clicked.connect(self.quitApp)


        #Form layout for buttons and labels
        lytForm = QFormLayout()
        lytForm.addRow(lblServices,cmbServices)
        lytForm.addRow(lblLandScape,cmbLandScape)
        lytForm.addRow(btnOpen)

        #Création du layout principal  de  la fenêtre(vertical)
        lytPrincipal = QVBoxLayout()
        lytPrincipal.addLayout(lytForm)
        lytPrincipal.addWidget(btnQuit)


        #vbox.addWidget(hboxServices)

        self.setLayout(lytPrincipal)

        #Set layout as the layout for the window
        #self.setCentralWidget(self,)

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showOpenFileDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Load file', '')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
    #Only the active windows closes, not the whole program
    def quitApp(self):
        self.close()


    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        self.center()

if __name__ == '__main__':
    qtApp = QApplication(sys.argv)
    ex = LeikertWindow()
    ex.run()
    sys.exit(qtApp.exec_())