from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget

class ChapterInformationPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.chapter_id_label = QLabel("Chapter ID:")
        self.chapter_id_edit = QLineEdit()
        layout.addWidget(self.chapter_id_label)
        layout.addWidget(self.chapter_id_edit)

        self.setLayout(layout)
