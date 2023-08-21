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
        add_choice_button.clicked.connect(lambda: self.add_choice())
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

    def add_choice(self, choice_text: str = "", next_chapter_id: int = None):
        if len(self.choices_widgets) < 6:
            choice_widget = ChoiceWidget()
            choice_widget.text_edit.setText(choice_text)
            choice_widget.next_chapter_id_edit.setText(str(next_chapter_id) if next_chapter_id is not None else "")
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