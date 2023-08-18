from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        info_label = QLabel("ERTG Writer\n\nVersion: 1.0\n\nA proprietary tool for Erainor RPG.\n© 2023 Envy Games")
        layout.addWidget(info_label)

        self.setLayout(layout)

        # Remove the context help button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)