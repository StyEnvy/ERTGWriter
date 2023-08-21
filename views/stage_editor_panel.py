from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QTextEdit, QStackedLayout, QHBoxLayout, QLineEdit, QLabel
from views.linear_stage_properties_editor import LinearStagePropertiesEditor
from views.input_stage_properties_editor import InputStagePropertiesEditor

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

    def build_stage(self):
        stage_id = int(self.stage_id_edit.text())
        stage_text = self.stage_text_editor.toPlainText()
        stage_type_index = self.stage_type_selector.currentIndex()

        # Linear Stage
        if stage_type_index == 0:
            next_stage_id_text = self.linear_properties_editor.next_stage_id_edit.text().strip()
            next_stage_id = int(next_stage_id_text) if next_stage_id_text.isdigit() else None
            properties = {'type': 'linear'}
            if next_stage_id is not None:
                properties['next_stage_id'] = next_stage_id
            stage_data = {
                'id': stage_id,
                'text': stage_text,
                'properties': properties
            }
        # Input Stage
        elif stage_type_index == 1:
            next_stage_id_text = self.input_properties_editor.next_stage_id_edit.text().strip()
            next_stage_id = int(next_stage_id_text) if next_stage_id_text.isdigit() else None
            input_key = self.input_properties_editor.input_key_edit.text().strip()
            special_case = self.input_properties_editor.special_case_edit.text().strip()
            special_case_next_chapter_id_text = self.input_properties_editor.special_case_next_chapter_id_edit.text().strip()
            special_case_next_chapter_id = int(special_case_next_chapter_id_text) if special_case_next_chapter_id_text.isdigit() else None

            # Extract choices
            choices = []
            for choice_widget in self.input_properties_editor.choices_widgets:
                choice_text = choice_widget.text_edit.text().strip()
                next_chapter_id_text = choice_widget.next_chapter_id_edit.text().strip()
                next_chapter_id = int(next_chapter_id_text) if next_chapter_id_text.isdigit() else None
                if choice_text:  # Only add choices if the text is not empty
                    choices.append({'text': choice_text, 'next_chapter_id': next_chapter_id})

            # Construct properties dictionary with required fields
            properties = {'type': 'input'}
            if next_stage_id is not None:
                properties['next_stage_id'] = next_stage_id
            if input_key:
                properties['input_key'] = input_key
            if special_case:
                properties['special_case'] = special_case
            if special_case_next_chapter_id is not None:
                properties['special_case_next_chapter_id'] = special_case_next_chapter_id
            if choices:
                properties['choices'] = choices

            stage_data = {
                'id': stage_id,
                'text': stage_text,
                'properties': properties
            }

        return stage_data
