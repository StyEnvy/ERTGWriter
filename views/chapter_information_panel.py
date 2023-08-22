from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget

class ChapterInformationPanel(QWidget): # Class to represent a chapter information panel
    def __init__(self): # Constructor
        super().__init__() # Call the parent constructor
        layout = QHBoxLayout() # Create a layout and set the spacing to 0

        self.chapter_id_label = QLabel("Chapter ID:") # Create a chapter ID label
        self.chapter_id_edit = QLineEdit() # Create a chapter ID field
        self.chapter_id_edit.setStyleSheet("font-size: 20px; color: black;") # Set the text color to black
        self.chapter_id_edit.setFixedWidth(100) # Set a fixed width for the chapter ID input

        layout.addWidget(self.chapter_id_label) # Add the chapter ID label to the horizontal layout
        layout.addWidget(self.chapter_id_edit) # Add the chapter ID field to the horizontal layout
        layout.addStretch() # Add a stretch to align the elements to the left

        self.setLayout(layout) # Set the main layout
