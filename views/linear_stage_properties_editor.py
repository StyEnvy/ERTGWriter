from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QSizePolicy

class LinearStagePropertiesEditor(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout and set the spacing to 0
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Next Stage ID
        next_stage_layout = QHBoxLayout()
        next_stage_layout.setSpacing(0)
        next_stage_label = QLabel("Next Stage ID:")
        self.next_stage_id_edit = QLineEdit()
        self.next_stage_id_edit.setStyleSheet("color: black;")
        next_stage_layout.addWidget(next_stage_label)
        next_stage_layout.addWidget(self.next_stage_id_edit)
        layout.addLayout(next_stage_layout)

        # Removing stretchable spacer
        # layout.addStretch(1)

        self.setLayout(layout)

        # Set the size policy so that the widget doesn't expand vertically
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) # Change to QSizePolicy.Maximum