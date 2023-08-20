from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QTextEdit, QStackedWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel

class StageEditorPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QVBoxLayout()

        # Stage Type Selector
        self.stage_type_selector = QComboBox()
        self.stage_type_selector.addItem("Linear")
        self.stage_type_selector.addItem("Input")
        layout.addWidget(self.stage_type_selector)

        # Label for stage text
        stage_text_label = QLabel("Write the stage text:")
        layout.addWidget(stage_text_label)

        # Stage Text Editor
        self.stage_text_editor = QTextEdit()
        layout.addWidget(self.stage_text_editor)

        # Properties Editor
        self.properties_editor = QStackedWidget()
        self.linear_properties_editor = LinearStagePropertiesEditor()
        self.input_properties_editor = InputStagePropertiesEditor()
        self.properties_editor.addWidget(self.linear_properties_editor)
        self.properties_editor.addWidget(self.input_properties_editor)
        layout.addWidget(self.properties_editor)

        self.stage_type_selector.currentIndexChanged.connect(self.properties_editor.setCurrentIndex)

        self.setLayout(layout)

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit

class LinearStagePropertiesEditor(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        # Next Stage ID
        self.next_stage_id_edit = QLineEdit()
        layout.addWidget(QLabel("Next Stage ID:"))
        layout.addWidget(self.next_stage_id_edit)

        self.setLayout(layout)

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTableWidget

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

        # Input Key
        self.input_key_edit = QLineEdit()
        layout.addWidget(QLabel("Input Key:"))
        layout.addWidget(self.input_key_edit)

        # Next Stage ID (optional)
        self.next_stage_id_edit = QLineEdit()
        layout.addWidget(QLabel("Next Stage ID (Optional):"))
        layout.addWidget(self.next_stage_id_edit)

        # Special Case (optional)
        self.special_case_edit = QLineEdit()
        layout.addWidget(QLabel("Special Case (Optional):"))
        layout.addWidget(self.special_case_edit)

        self.setLayout(layout)

    def add_choice(self):
        if len(self.choices_widgets) < 6:
            choice_widget = ChoiceWidget()
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
        layout.addWidget(self.text_edit)

        self.next_chapter_id_edit = QLineEdit()
        layout.addWidget(QLabel("Next Chapter ID:"))
        layout.addWidget(self.next_chapter_id_edit)

        self.setLayout(layout)
