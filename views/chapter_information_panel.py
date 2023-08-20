from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget

class ChapterInformationPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.chapter_id_label = QLabel("Chapter ID:")
        self.chapter_id_edit = QLineEdit()
        self.chapter_id_edit.setStyleSheet("color: black;")
        self.chapter_id_edit.setFixedWidth(100) # Set a fixed width for the chapter ID input

        layout.addWidget(self.chapter_id_label)
        layout.addWidget(self.chapter_id_edit)
        layout.addStretch() # Add a stretch to align the elements to the left

        self.setLayout(layout)
