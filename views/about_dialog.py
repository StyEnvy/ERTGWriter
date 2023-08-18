from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class AboutDialog(QDialog):
    def __init__(self): # Accept parent window
        super().__init__() # Call the parent QDialog constructor

        layout = QVBoxLayout() # Create a layout for the dialog

        info_label = QLabel("ERTG Writer\n\nVersion: 1.0\n\nA proprietary tool for Erainor RPG.\n© 2023 Envy Games") # Create a label
        layout.addWidget(info_label) # Add the label to the layout

        self.setLayout(layout) # Set the layout for the dialog

        # Remove the context help button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint) # Remove the context help button