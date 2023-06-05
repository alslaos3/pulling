import os
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QListWidget, QPushButton, QListWidgetItem
from PySide6.QtCore import Qt, Slot, Signal
from sequenceEditWindow import SequenceEditWidget

class SequenceWidget(QWidget):

    def __init__(self):
        super(SequenceWidget, self).__init__()

        self.sequenceList = QListWidget()
        self.sequenceEditWidget = SequenceEditWidget()
        self.sequenceList.itemClicked.connect(self.sequenceEditWidget.show)
        self.sequenceList.itemClicked.connect(self.onItemClicked)

        self.btnAddSequence = QPushButton("Add Sequence")
        self.btnDeleteSequence = QPushButton("Delete Sequence")
        self.btnSortSequence = QPushButton("Sort")
        self.btnAddSequence.clicked.connect(self.addSequence)
        self.btnDeleteSequence.clicked.connect(self.deleteSequence)
        self.btnSortSequence.clicked.connect(self.sortSequence)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.sequenceList)
        self.layout.addWidget(self.btnAddSequence)
        self.layout.addWidget(self.btnDeleteSequence)
        self.layout.addWidget(self.btnSortSequence)

        self.setLayout(self.layout)

        self.loadSequences()

    def onItemClicked(self, item: QListWidgetItem):
        sequence_dir = "sequence"
        sequence_name = item.text()
        sequence_file = sequence_dir + "/" + sequence_name
        self.sequenceEditWidget.setSequenceName(sequence_file)
        self.sequenceEditWidget.loadSequence(sequence_file)

    def loadSequences(self):
        sequence_dir = "sequence"  # 시퀀스 파일이 있는 디렉토리 경로
        sequences = os.listdir(sequence_dir)
        self.sequenceList.clear()
        for sequence in sequences:
            self.sequenceList.addItem(sequence[:-4])

    def addSequence(self):
        sequence_dir = "sequence"  # 시퀀스 파일을 저장할 디렉토리 경로
        sequence_base_name = "sequence_{}.txt"  # 시퀀스 파일의 기본 이름 형식
        i = 1
        while True:
            sequence_name = sequence_base_name.format(i)
            sequence_path = os.path.join(sequence_dir, sequence_name)
            if not os.path.exists(sequence_path):
                break
            i += 1

        with open(sequence_path, "w") as f:
            f.write("")

        sequence_item = QListWidgetItem(sequence_name.replace(".txt",""))
        self.sequenceList.addItem(sequence_item)

    def deleteSequence(self):
        selected_items = self.sequenceList.selectedItems()
        if not selected_items:
            return

        sequence_dir = "sequence"  # 시퀀스 파일이 저장된 디렉토리 경로

        for item in selected_items:
            sequence_name = item.text() + ".txt"
            sequence_path = os.path.join(sequence_dir, sequence_name)

            if os.path.exists(sequence_path):
                os.remove(sequence_path)

            self.sequenceList.takeItem(self.sequenceList.row(item))

    def sortSequence(self):
        items = []
        for i in range(self.sequenceList.count()):
            items.append(self.sequenceList.item(i).text())

        sorted_texts = sorted(items)

        self.sequenceList.clear()
        self.sequenceList.addItems(sorted_texts)


if __name__ == '__main__':
    app = QApplication([])
    w = SequenceWidget()
    w.show()
    app.exec()
