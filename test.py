from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QFont, Qt

class LogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Window")

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)  # 칼럼 개수 설정
        self.table_widget.setRowCount(10)  # 행 개수 설정

        self.set_table_headers()

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_table_headers(self):
        header_labels = ["No.", "Type", "제작일", "배양일", "농도", "사용횟수"]
        category_labels = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6"]

        for col, label in enumerate(header_labels):
            header_item = QTableWidgetItem(label)
            self.table_widget.setHorizontalHeaderItem(col, header_item)

        for col, label in enumerate(category_labels):
            category_label = QLabel(label)
            category_label.setAlignment(Qt.AlignCenter)
            category_label.setFont(QFont("Arial", 8, QFont.Bold))
            self.table_widget.setCellWidget(1, col, category_label)

if __name__ == '__main__':
    app = QApplication([])
    window = LogWindow()
    window.show()
    app.exec()
