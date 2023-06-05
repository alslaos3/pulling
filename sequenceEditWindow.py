from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class SequenceEditWidget(QWidget):
    def __init__(self):
        super(SequenceEditWidget, self).__init__()

        self.stepTable = QTableWidget()
        self.stepTable.cellChanged.connect(self.saveSequence)
        self.stepTable.setColumnCount(3)
        self.stepTable.setHorizontalHeaderLabels(["Step No.", "Distance", "Velocity"])

        self.btnAddStep = QPushButton("Add Step")
        self.btnDeleteStep = QPushButton("Delete Step")
        self.btnAddStep.clicked.connect(self.addStep)
        self.btnDeleteStep.clicked.connect(self.deleteStep)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stepTable)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btnAddStep)
        button_layout.addWidget(self.btnDeleteStep)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        self.steps = []

        self.addStep()  # Add initial step

        self.sequence_name = ""

    def addStep(self):
        step_no = self.stepTable.rowCount() + 1

        self.stepTable.setRowCount(step_no)

        step_no_item = QTableWidgetItem(str(step_no))
        step_no_item.setFlags(Qt.ItemIsEnabled)
        self.stepTable.setItem(step_no - 1, 0, step_no_item)

        distance_item = QTableWidgetItem()
        self.stepTable.setItem(step_no - 1, 1, distance_item)

        velocity_item = QTableWidgetItem()
        self.stepTable.setItem(step_no - 1, 2, velocity_item)

        self.steps.append((step_no_item, distance_item, velocity_item))

    def deleteStep(self):
        selected_rows = []
        for item in self.stepTable.selectedItems():
            if item.row() not in selected_rows:
                selected_rows.append(item.row())

        for row in selected_rows:
            self.stepTable.removeRow(row)
            self.steps.pop(row)

        # Update step numbers
        for row in range(self.stepTable.rowCount()):
            step_no_item = QTableWidgetItem(str(row + 1))
            step_no_item.setFlags(Qt.ItemIsEnabled)
            self.stepTable.setItem(row, 0, step_no_item)
            self.steps[row] = (step_no_item, self.steps[row][1], self.steps[row][2])

    def setSequenceName(self, sequence_name):
        self.sequence_name = sequence_name

    def loadSequence(self, sequence_file):
        sequence_file = f"{self.sequence_name}.txt"
        self.stepTable.clearContents()
        self.stepTable.setRowCount(0)
        self.steps = []

        with open(sequence_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    step_data = line.split(",")
                    step_no = step_data[0]
                    distance = step_data[1]
                    velocity = step_data[2]

                    self.addStep()
                    row = self.stepTable.rowCount() - 1

                    step_no_item = self.stepTable.item(row, 0)
                    step_no_item.setText(step_no)

                    distance_item = self.stepTable.item(row, 1)
                    distance_item.setText(distance)

                    velocity_item = self.stepTable.item(row, 2)
                    velocity_item.setText(velocity)

    def saveSequence(self, sequence_file):
        try:
            sequence_file = f"{self.sequence_name}.txt"
            with open(sequence_file, "w") as f:
                for step in self.steps:
                    step_no = step[0].text()
                    distance = step[1].text()
                    velocity = step[2].text()
                    f.write(f"{step_no},{distance},{velocity}\n")
        except AttributeError:
            print("initiating")