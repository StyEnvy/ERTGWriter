from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QTextEdit, QStackedLayout, QHBoxLayout, QLineEdit, QLabel
from views.linear_stage_properties_editor import LinearStagePropertiesEditor
from views.input_stage_properties_editor import InputStagePropertiesEditor

class StageEditorPanel(QWidget): # Class to represent a stage editor panel
    def __init__(self): # Constructor
        super().__init__() # Call the parent constructor

        # Main layout
        layout = QVBoxLayout() # Create a main layout

        # Stage ID Label and Field (Horizontal Layout)
        stage_id_layout = QHBoxLayout() # Create a horizontal layout
        stage_id_label = QLabel("Stage ID:") # Create a stage ID label
        stage_id_label.setStyleSheet("font-size: 16px;") # Set the font size
        self.stage_id_edit = QLineEdit() # Create a stage ID field
        self.stage_id_edit.setFixedWidth(100) # Set a fixed width
        self.stage_id_edit.setStyleSheet("font-size: 16px; color: black;") # Set the text color to black
        stage_id_layout.addWidget(stage_id_label) # Add the stage ID label to the horizontal layout
        stage_id_layout.addWidget(self.stage_id_edit) # Add the stage ID field to the horizontal layout
        layout.addLayout(stage_id_layout) # Add the horizontal layout to the main layout

        # Stage Type Selector
        self.stage_type_selector = QComboBox() # Create a stage type selector
        self.stage_type_selector.addItem("Linear") # Add the linear stage type
        self.stage_type_selector.setStyleSheet("font-size: 16px; color: black; background-color: white;") # Set the text color to black
        self.stage_type_selector.addItem("Input") # Add the input stage type
        self.stage_type_selector.setStyleSheet("font-size: 16px; color: black; background-color: white;") # Set the text color to black
        layout.addWidget(self.stage_type_selector) # Add the stage type selector to the main layout

        # Label for stage text
        stage_text_label = QLabel("Write the stage text:") # Create a label for the stage text
        stage_text_label.setStyleSheet("font-size: 16px;") # Set the font size
        layout.addWidget(stage_text_label) # Add the label to the main layout

        # Stage Text Editor
        self.stage_text_editor = QTextEdit() # Create a stage text editor
        self.stage_text_editor.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.stage_text_editor) # Add the stage text editor to the main layout

        # Properties Editor
        self.properties_layout = QStackedLayout() # Create a stacked layout for the properties editor
        self.properties_layout.setSizeConstraint(QStackedLayout.SetMinAndMaxSize) # Set size constraint
        self.linear_properties_editor = LinearStagePropertiesEditor() # Create a linear stage properties editor
        self.input_properties_editor = InputStagePropertiesEditor() # Create an input stage properties editor
        self.properties_layout.addWidget(self.linear_properties_editor) # Add the linear stage properties editor to the stacked layout
        self.properties_layout.addWidget(self.input_properties_editor) # Add the input stage properties editor to the stacked layout
        layout.addLayout(self.properties_layout) # Add the stacked layout to the main layout

        self.stage_type_selector.currentIndexChanged.connect(self.properties_layout.setCurrentIndex) # Connect the stage type selector to the stacked layout

        self.setLayout(layout) # Set the main layout

    def build_stage(self): # Function to build the stage
        stage_id = int(self.stage_id_edit.text()) # Get the stage ID
        stage_text = self.stage_text_editor.toPlainText() # Get the stage text
        stage_type_index = self.stage_type_selector.currentIndex() # Get the stage type index

        # Linear Stage
        if stage_type_index == 0: # Linear stage
            next_stage_id_text = self.linear_properties_editor.next_stage_id_edit.text().strip() # Get the next stage ID
            next_stage_id = int(next_stage_id_text) if next_stage_id_text.isdigit() else None # Convert the next stage ID to an integer if it is a number, otherwise None
            properties = {'type': 'linear'}
            if next_stage_id is not None:
                properties['next_stage_id'] = next_stage_id
            stage_data = {'id': stage_id, 'text': stage_text, 'properties': properties} # Create the stage data

        # Input Stage
        elif stage_type_index == 1: # Input stage
            input_key = self.input_properties_editor.input_key_edit.text().strip() # Get the input key
            special_case = self.input_properties_editor.special_case_edit.text().strip() # Get the special case
            special_case_next_chapter_id_text = self.input_properties_editor.special_case_next_chapter_id_edit.text().strip() # Get the special case next chapter ID
            special_case_next_chapter_id = int(special_case_next_chapter_id_text) if special_case_next_chapter_id_text.isdigit() else None # Convert the special case next chapter ID to an integer if it is a number, otherwise None

            next_stage_id_text = self.input_properties_editor.next_stage_id_edit.text().strip() # Get the next stage ID outside the choice widget
            next_stage_id = int(next_stage_id_text) if next_stage_id_text.isdigit() else None # Convert the next stage ID to an integer if it is a number, otherwise None

            # Extract choices
            choices = [] # Create a list of choices
            for choice_widget in self.input_properties_editor.choices_widgets: # Loop through the choice widgets
                choice_text = choice_widget.text_edit.text().strip() # Get the choice text

                # Skip the choice if the text is None or empty
                if not choice_text:
                    continue

                next_choice_stage_id_text = choice_widget.next_stage_id_edit.text().strip() # Get the next stage ID for the choice
                next_choice_stage_id = int(next_choice_stage_id_text) if next_choice_stage_id_text.isdigit() else None # Convert the next stage ID to an integer if it is a number, otherwise None

                next_chapter_id_text = choice_widget.next_chapter_id_edit.text().strip() # Get the next chapter ID
                next_chapter_id = int(next_chapter_id_text) if next_chapter_id_text.isdigit() else None # Convert the next chapter ID to an integer if it is a number, otherwise None

                choice_data = {'text': choice_text}
                if next_choice_stage_id is not None:
                    choice_data['next_stage_id'] = next_choice_stage_id
                if next_chapter_id is not None:
                    choice_data['next_chapter_id'] = next_chapter_id

                choices.append(choice_data) # Add the choice to the list

            # Construct properties dictionary with required fields
            properties = {'type': 'input', 'input_key': input_key}
            if choices:
                properties['choices'] = choices
            if next_stage_id is not None:
                properties['next_stage_id'] = next_stage_id
            if special_case != "None" and special_case:
                properties['special_case'] = special_case
            if special_case_next_chapter_id is not None:
                properties['special_case_next_chapter_id'] = special_case_next_chapter_id

            stage_data = {'id': stage_id, 'text': stage_text, 'properties': properties} # Create the stage data

        return stage_data # Return the stage data



