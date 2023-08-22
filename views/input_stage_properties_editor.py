from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class InputStagePropertiesEditor(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() # Create a layout and set the spacing to 0

        # Choices Layout
        self.choices_widgets = [] # List to store the choice widgets
        choices_label = QLabel("Add a new choice field:") # Create a label for the choices
        choices_label.setStyleSheet("font-size: 16px;") # Set the font size
        layout.addWidget(choices_label) # Add the label to the main layout

        # Add/Remove Choice Buttons
        choice_buttons_layout = QHBoxLayout() # Create a choice buttons layout
        add_choice_button = QPushButton("Add") # Create an add choice button
        add_choice_button.setStyleSheet("font-size: 16px;") # Set the font size
        add_choice_button.setFixedWidth(80) # Set a fixed width
        add_choice_button.clicked.connect(lambda: self.add_choice()) # Connect the add choice button to the add choice function
        remove_choice_button = QPushButton("Remove") # Create a remove choice button
        remove_choice_button.setStyleSheet("font-size: 16px;") # Set the font size
        remove_choice_button.setFixedWidth(80) # Set a fixed width
        remove_choice_button.clicked.connect(self.remove_choice) # Connect the remove choice button to the remove choice function
        choice_buttons_layout.addWidget(add_choice_button) # Add the choice buttons to the choice buttons layout
        choice_buttons_layout.addWidget(remove_choice_button) # Add the choice buttons to the choice buttons layout
        layout.addLayout(choice_buttons_layout) # Add the choice buttons layout to the main layout

        # Input Key (optional)
        input_key_label = QLabel("Input Key (Optional):")
        input_key_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(input_key_label)
        self.input_key_edit = QLineEdit()
        self.input_key_edit.setStyleSheet("font-size: 16px; color: black;")
        layout.addWidget(self.input_key_edit)

        # Next Stage ID (optional)
        next_stage_id_label = QLabel("Next Stage ID (Optional):")
        next_stage_id_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(next_stage_id_label)
        self.next_stage_id_edit = QLineEdit()
        self.next_stage_id_edit.setStyleSheet("font-size: 16px; color: black;")
        layout.addWidget(self.next_stage_id_edit)

        # Special Case (optional)
        special_case_label = QLabel("Special Case (Optional):")
        special_case_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(special_case_label)
        self.special_case_edit = QLineEdit()
        self.special_case_edit.setStyleSheet("font-size: 16px; color: black;")
        layout.addWidget(self.special_case_edit)

        # Special Case Next Chapter ID (optional)
        special_case_next_chapter_id_label = QLabel("Special Case Next Chapter ID (Optional):")
        special_case_next_chapter_id_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(special_case_next_chapter_id_label)
        self.special_case_next_chapter_id_edit = QLineEdit()
        self.special_case_next_chapter_id_edit.setStyleSheet("font-size: 16px; color: black;")
        layout.addWidget(self.special_case_next_chapter_id_edit)

        self.setLayout(layout)

    def add_choice(self, choice_text: str = "", next_chapter_id: int = None, next_stage_id: int = None): # Function to add a choice
        if len(self.choices_widgets) < 6: # If there are less than 6 choices
            choice_widget = ChoiceWidget() # Create a choice widget
            choice_widget.text_edit.setText(choice_text) # Set the choice text
            choice_widget.next_chapter_id_edit.setText(str(next_chapter_id) if next_chapter_id is not None else "") # Set the next chapter ID
            choice_widget.next_stage_id_edit.setText(str(next_stage_id) if next_stage_id is not None else "") # Set the next stage ID
            self.choices_widgets.append(choice_widget) # Add the choice widget to the list
            self.layout().insertWidget(len(self.choices_widgets), choice_widget) # Add the choice widget to the layout
            if len(self.choices_widgets) == 6: # If there are 6 choices
                sender = self.sender() # Get the sender
                sender.setDisabled(True) # Disable the sender

    def remove_choice(self): # Function to remove a choice
        if self.choices_widgets: # If there are choices
            choice_widget = self.choices_widgets.pop() # Remove the last choice widget from the list
            choice_widget.deleteLater() # Delete the choice widget

class ChoiceWidget(QWidget): # Widget to store a choice
    def __init__(self): # Constructor
        super().__init__() # Call the parent constructor
        layout = QHBoxLayout() # Create a layout

        self.text_edit = QLineEdit() # Create a text edit
        layout.addWidget(QLabel("Choice Text:")) # Add a label for the text edit
        self.text_edit.setStyleSheet("font-size: 16px; color: black;") # Set the text color to black
        layout.addWidget(self.text_edit) # Add the text edit to the layout

        self.next_chapter_id_edit = QLineEdit() # Create a next chapter ID edit
        layout.addWidget(QLabel("Next Chapter ID:")) # Add a label for the next chapter ID edit
        self.next_chapter_id_edit.setStyleSheet("font-size: 16px; color: black;") # Set the text color to black
        layout.addWidget(self.next_chapter_id_edit) # Add the next chapter ID edit to the layout

        self.next_stage_id_edit = QLineEdit() # Create a next stage ID edit
        layout.addWidget(QLabel("Next Stage ID:")) # Add a label for the next stage ID edit
        self.next_stage_id_edit.setStyleSheet("font-size: 16px; color: black;") # Set the text color to black
        layout.addWidget(self.next_stage_id_edit) # Add the next stage ID edit to the layout

        self.setLayout(layout) # Set the layout