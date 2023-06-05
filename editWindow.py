from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, \
    QCalendarWidget
from PySide6.QtCore import Qt, Slot, Signal

class ExpTableWidget(QWidget):

    HEADER = ["No.","Type","배양일","농도(㎎/㎖)","사용 횟수(회)", "추가 전처리", "온도(℃)", "습도(%)","사용 기계","기판 너비(㎜)","길이(㎜)","Speed (㎛/min)"]
    initTableHeight = 0
    def __init__(self):
        super(ExpTableWidget, self).__init__()

        self.expTableWidget = QTableWidget()
        self.expTableWidget.setColumnCount(len(self.HEADER))
        self.expTableWidget.setHorizontalHeaderLabels(self.HEADER)
        self.expTableWidget.itemDoubleClicked.connect(self.showCalendarWidget)
        self.expTableWidget.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.SelectedClicked | QTableWidget.AnyKeyPressed)


        # self.btnAddRow.setFixedWidth(20)

        self.calendarWidget = QCalendarWidget()
        self.calendarWidget.clicked.connect(self.setCellDate)
        self.calendarWidget.setVisible(False)

        hbox = QHBoxLayout()
        hbox.addWidget(self.calendarWidget)
        hbox.addWidget(self.expTableWidget)
        self.setLayout(hbox)

        self.loadLog()

        for col in range(self.expTableWidget.columnCount()):
            self.expTableWidget.resizeColumnToContents(col)

        self.resizeTableWidget(True)
        self.originalSize = self.size()

    def showCalendarWidget(self, item):
        if item.column() == self.HEADER.index("배양일"):
            self.selectedItem = item
            self.calendarWidget.show()

    def setCellDate(self, date):
        selectedDate = date.toString(Qt.ISODate)
        self.selectedItem.setText(selectedDate)
        # self.calendarWidget.hide()
        self.calendarWidget.setVisible(False)
        self.resize(self.originalSize)

    @Slot()
    def addRow(self):
        row = self.expTableWidget.rowCount()
        self.expTableWidget.insertRow(row)
        for col in range(self.expTableWidget.columnCount()):
            item = QTableWidgetItem()
            if col == 0:
                item.setText(str(row+1))
            self.expTableWidget.setItem(row, col, item)
            self.expTableWidget.resizeColumnToContents(col)
            self.resizeTableWidget()

    def resizeTableWidget(self,init=False):
        tableWidth = self.expTableWidget.horizontalHeader().length()
        tableHeight = self.expTableWidget.verticalHeader().length()

        if init:
            self.initTableHeight = self.expTableWidget.height()
            # self.setFixedSize(tableWidth, tableHeight)
            self.resize(tableWidth, tableHeight)
        else:
            pass

    def saveLog(self, row, col):
        logData = []
        for row in range(self.expTableWidget.rowCount()):
            eachRow = []
            for col in range(self.expTableWidget.columnCount()):
                item = self.expTableWidget.item(row, col)
                if item is None:
                    item = QTableWidgetItem(" ")
                eachRow.append(item.text())
            logData.append(eachRow)

        with open("log.txt", "w") as f:
            for row in logData:
                f.write("\t".join(row) + "\n")


    def loadLog(self):
        try:
            with open("log.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    row_data = line.strip().split("\t")
                    self.addRow()
                    row = self.expTableWidget.rowCount() - 1
                    for col, data in enumerate(row_data):
                        item = QTableWidgetItem(data)
                        self.expTableWidget.setItem(row, col, item)
        except FileNotFoundError:
            print("log.txt 파일이 존재하지 않습니다. 새로 작성합니다.")

        finally:
            self.expTableWidget.cellChanged.connect(self.saveLog)

if __name__ == '__main__':
    app = QApplication([])
    w = ExpTableWidget()
    w.show()
    app.exec()
