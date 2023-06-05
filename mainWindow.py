from PySide6.QtWidgets import QMainWindow, QListView, QPlainTextEdit, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox
# from PySide6.QtCore import
# from PySide6.QtGui import
from editWindow import ExpTableWidget
from sequenceWindow import SequenceWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.initSignalSlot()
        self.initResize()

    def initUI(self):
        self.centralWidget = QWidget()
        self.expList = QListView()
        self.statusLog = QPlainTextEdit()
        self.expTableWidget = ExpTableWidget()
        self.sequenceWidget = SequenceWidget()

        self.btnAddRow = QPushButton("Add Experiment")
        self.btnJogUp = QPushButton("Jog(+)")
        self.btnJogDown = QPushButton("Jog(-)")
        self.btnDriveUp = QPushButton("Drive(+)")
        self.btnDriveDown = QPushButton("Drive(-)")
        self.btnStartSequence = QPushButton("Sequence Start")
        self.btnStopSequence = QPushButton("Sequence Stop")
        self.btnEditSequence = QPushButton("Edit Sequence")
        self.btnMoveHome = QPushButton("Home")

        self.groupBoxBar = QGroupBox()
        vboxBar = QVBoxLayout()
        vboxBar.addWidget(self.btnAddRow)
        vboxBar.addWidget(self.btnEditSequence)
        self.groupBoxBar.setLayout(vboxBar)

        self.groupBoxMotor = QGroupBox()
        vboxMotor = QVBoxLayout()
        vboxMotor.addWidget(self.btnDriveUp)
        vboxMotor.addWidget(self.btnJogUp)
        vboxMotor.addWidget(self.btnMoveHome)
        vboxMotor.addWidget(self.btnJogDown)
        vboxMotor.addWidget(self.btnDriveDown)
        self.groupBoxMotor.setLayout(vboxMotor)

        self.groupBoxRun = QGroupBox()
        hboxRun = QHBoxLayout()
        hboxRun.addWidget(self.btnStartSequence)
        hboxRun.addWidget(self.btnStopSequence)
        self.groupBoxRun.setLayout(hboxRun)

        self.controlWidget = QWidget()
        hboxControl = QHBoxLayout()
        vboxControl = QVBoxLayout()
        hboxControl.addWidget(self.groupBoxBar)
        hboxControl.addWidget(self.groupBoxMotor)
        vboxControl.addLayout(hboxControl)
        vboxControl.addWidget(self.groupBoxRun)
        self.controlWidget.setLayout(vboxControl)

        hbox = QHBoxLayout()
        hbox.addWidget(self.expTableWidget)
        hbox.addWidget(self.controlWidget)
        self.centralWidget.setLayout(hbox)
        self.setCentralWidget(self.centralWidget)

    def initSignalSlot(self):
        self.btnAddRow.clicked.connect(self.expTableWidget.addRow)
        self.btnEditSequence.clicked.connect(self.sequenceWidget.show)

    def initResize(self):
        self.resize(self.expTableWidget.size())

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()