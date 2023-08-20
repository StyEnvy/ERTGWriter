from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QTextEdit, QStackedLayout, QHBoxLayout, QLineEdit, QLabel, QSizePolicy

class StageEditorPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QVBoxLayout()

        # Stage ID Label and Field (Horizontal Layout)
        stage_id_layout = QHBoxLayout()
        stage_id_label = QLabel("Stage ID:")
        self.stage_id_edit = QLineEdit()
        self.stage_id_edit.setFixedWidth(100) # Set a fixed width
        self.stage_id_edit.setStyleSheet("color: black;")
        stage_id_layout.addWidget(stage_id_label)
        stage_id_layout.addWidget(self.stage_id_edit)
        layout.addLayout(stage_id_layout)

        # Stage Type Selector
        self.stage_type_selector = QComboBox()
        self.stage_type_selector.addItem("Linear")
        self.stage_type_selector.addItem("Input")
        self.stage_type_selector.setStyleSheet("color: black;") # Set the text color to black
        layout.addWidget(self.stage_type_selector)

        # Label for stage text
        stage_text_label = QLabel("Write the stage text:")
        layout.addWidget(stage_text_label)

        # Stage Text Editor
        self.stage_text_editor = QTextEdit()
        layout.addWidget(self.stage_text_editor)

        # Properties Editor
        self.properties_layout = QStackedLayout()
        self.properties_layout.setSizeConstraint(QStackedLayout.SetMinAndMaxSize) # Set size constraint
        self.linear_properties_editor = LinearStagePropertiesEditor()
        self.input_properties_editor = InputStagePropertiesEditor()
        self.properties_layout.addWidget(self.linear_properties_editor)
        self.properties_layout.addWidget(self.input_properties_editor)
        layout.addLayout(self.properties_layout)

        self.stage_type_selector.currentIndexChanged.connect(self.properties_layout.setCurrentIndex)

        self.setLayout(layout)

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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class InputStagePropertiesEditor(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Choices Layout
        self.choices_widgets = []
        choices_label = QLabel("Add a new choice field:")
        layout.addWidget(choices_label)

        # Add/Remove Choice Buttons
        choice_buttons_layout = QHBoxLayout()
        add_choice_button = QPushButton("Add")
        add_choice_button.setFixedWidth(80)
        add_choice_button.clicked.connect(self.add_choice)
        remove_choice_button = QPushButton("Remove")
        remove_choice_button.setFixedWidth(80)
        remove_choice_button.clicked.connect(self.remove_choice)
        choice_buttons_layout.addWidget(add_choice_button)
        choice_buttons_layout.addWidget(remove_choice_button)
        layout.addLayout(choice_buttons_layout)

        # Input Key  (optional)
        self.input_key_edit = QLineEdit()
        layout.addWidget(QLabel("Input Key (Optional):"))
        self.input_key_edit.setStyleSheet("color: black;")
        layout.addWidget(self.input_key_edit)

        # Next Stage ID (optional)
        self.next_stage_id_edit = QLineEdit()
        layout.addWidget(QLabel("Next Stage ID (Optional):"))
        self.next_stage_id_edit.setStyleSheet("color: black;")
        layout.addWidget(self.next_stage_id_edit)

        # Special Case (optional)
        self.special_case_edit = QLineEdit()
        layout.addWidget(QLabel("Special Case (Optional):"))
        self.special_case_edit.setStyleSheet("color: black;")
        layout.addWidget(self.special_case_edit)

        # Special Case Next Chapter ID (optional)
        self.special_case_next_chapter_id_edit = QLineEdit()
        layout.addWidget(QLabel("Special Case Next Chapter ID (Optional):"))
        self.special_case_next_chapter_id_edit.setStyleSheet("color: black;")
        layout.addWidget(self.special_case_next_chapter_id_edit)

        self.setLayout(layout)

    def add_choice(self, choice_text: str, next_chapter_id: int):
        if len(self.choices_widgets) < 6:
            choice_widget = ChoiceWidget()
            choice_widget.text_edit.setText(choice_text)
            choice_widget.next_chapter_id_edit.setText(str(next_chapter_id))
            self.choices_widgets.append(choice_widget)
            self.layout().insertWidget(len(self.choices_widgets), choice_widget)
            if len(self.choices_widgets) == 6:
                sender = self.sender()
                sender.setDisabled(True)

    def remove_choice(self):
        if self.choices_widgets:
            choice_widget = self.choices_widgets.pop()
            choice_widget.deleteLater()

class ChoiceWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.text_edit = QLineEdit()
        layout.addWidget(QLabel("Choice Text:"))
        self.text_edit.setStyleSheet("color: black;")
        layout.addWidget(self.text_edit)

        self.next_chapter_id_edit = QLineEdit()
        layout.addWidget(QLabel("Next Chapter ID:"))
        self.next_chapter_id_edit.setStyleSheet("color: black;")
        layout.addWidget(self.next_chapter_id_edit)

        self.setLayout(layout)
