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
            properties = {'type': 'linear'} # Create a properties dictionary with the required fields
            if next_stage_id is not None: # If the next stage ID is not None
                properties['next_stage_id'] = next_stage_id # Add the next stage ID to the properties dictionary
            stage_data = { # Create the stage data
                'id': stage_id, # Add the stage ID
                'text': stage_text, # Add the stage text
                'properties': properties # Add the properties
            }
        # Input Stage
        elif stage_type_index == 1: # Input stage
            next_stage_id_text = self.input_properties_editor.next_stage_id_edit.text().strip() # Get the next stage ID
            next_stage_id = int(next_stage_id_text) if next_stage_id_text.isdigit() else None # Convert the next stage ID to an integer if it is a number, otherwise None
            input_key = self.input_properties_editor.input_key_edit.text().strip() # Get the input key
            special_case = self.input_properties_editor.special_case_edit.text().strip() # Get the special case
            special_case_next_chapter_id_text = self.input_properties_editor.special_case_next_chapter_id_edit.text().strip() # Get the special case next chapter ID
            special_case_next_chapter_id = int(special_case_next_chapter_id_text) if special_case_next_chapter_id_text.isdigit() else None # Convert the special case next chapter ID to an integer if it is a number, otherwise None

            # Extract choices
            choices = [] # Create a list of choices
            for choice_widget in self.input_properties_editor.choices_widgets: # Loop through the choice widgets
                choice_text = choice_widget.text_edit.text().strip() # Get the choice text
                next_chapter_id_text = choice_widget.next_chapter_id_edit.text().strip() # Get the next chapter ID
                next_chapter_id = int(next_chapter_id_text) if next_chapter_id_text.isdigit() else None # Convert the next chapter ID to an integer if it is a number, otherwise None
                if choice_text:  # Only add choices if the text is not empty
                    choices.append({'text': choice_text, 'next_chapter_id': next_chapter_id}) # Add the choice to the list

            # Construct properties dictionary with required fields
            properties = {'type': 'input'} # Create a properties dictionary with the required fields
            if next_stage_id is not None: # If the next stage ID is not None
                properties['next_stage_id'] = next_stage_id # Add the next stage ID to the properties dictionary
            if input_key: # If the input key is not empty
                properties['input_key'] = input_key # Add the input key to the properties dictionary
            if special_case: # If the special case is not empty
                properties['special_case'] = special_case # Add the special case to the properties dictionary
            if special_case_next_chapter_id is not None: # If the special case next chapter ID is not None
                properties['special_case_next_chapter_id'] = special_case_next_chapter_id # Add the special case next chapter ID to the properties dictionary
            if choices: # If there are choices
                properties['choices'] = choices # Add the choices to the properties dictionary

            stage_data = { # Create the stage data
                'id': stage_id, # Add the stage ID
                'text': stage_text, # Add the stage text
                'properties': properties # Add the properties
            }

        return stage_data # Return the stage data
