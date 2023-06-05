import sys
from mainWindow import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec())