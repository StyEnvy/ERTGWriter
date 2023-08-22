from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QSizePolicy

class LinearStagePropertiesEditor(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout and set the spacing to 0
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0) # Set the margins to 0

        # Next Stage ID
        next_stage_layout = QHBoxLayout() # Create a horizontal layout
        next_stage_layout.setSpacing(0) # Set the spacing to 0
        next_stage_label = QLabel("Next Stage ID:") # Create a next stage ID label
        next_stage_label.setStyleSheet("font-size: 16px;")
        self.next_stage_id_edit = QLineEdit() # Create a next stage ID field
        self.next_stage_id_edit.setStyleSheet("font-size: 16px; color: black;") # Set the text color to black
        next_stage_layout.addWidget(next_stage_label) # Add the next stage ID label to the horizontal layout
        next_stage_layout.addWidget(self.next_stage_id_edit) # Add the next stage ID field to the horizontal layout
        layout.addLayout(next_stage_layout) # Add the next stage layout to the main layout

        # Removing stretchable spacer
        # layout.addStretch(1)

        self.setLayout(layout)

        # Set the size policy so that the widget doesn't expand vertically
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) # Change to QSizePolicy.Maximum