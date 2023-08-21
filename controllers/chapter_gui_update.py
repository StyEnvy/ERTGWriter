from models.chapter import LinearStage, InputStage
from views.stage_editor_panel import StageEditorPanel
from PyQt5.QtWidgets import QFrame

class ChapterGUIUpdater:
    def __init__(self, view):
        self.view = view

    def update_gui_with_chapter(self, chapter, file_path: str): # Function to update the GUI with a chapter
        chapter_id = file_path.split("_")[-1].split(".")[0]  # Extract chapter ID from file path
        self.view.chapter_info_panel.chapter_id_edit.setText(chapter_id) # Set the chapter ID

        # Clear existing stages
        while self.view.stage_editor_container.count() > 0: 
            item = self.view.stage_editor_container.takeAt(0) 
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Add loaded stages to StageEditorContainer
        for stage in chapter.stages: # Loop through the stages
            stage_editor_panel = StageEditorPanel() # Create a StageEditorPanel

            # Set the stage ID
            stage_editor_panel.stage_id_edit.setText(str(stage.stage_id)) 

            # Set the stage text
            stage_editor_panel.stage_text_editor.setText(stage.text)

            # Set the stage type and properties
            if isinstance(stage, LinearStage): # Linear stage
                stage_editor_panel.stage_type_selector.setCurrentIndex(0) # Set the stage type selector to Linear
                stage_editor_panel.linear_properties_editor.next_stage_id_edit.setText(str(stage.next_stage_id)) # Set the next stage ID
            elif isinstance(stage, InputStage): # Input stage
                stage_editor_panel.stage_type_selector.setCurrentIndex(1) # Set the stage type selector to Input
                stage_editor_panel.input_properties_editor.next_stage_id_edit.setText(str(stage.next_stage_id)) # Set the next stage ID
                stage_editor_panel.input_properties_editor.input_key_edit.setText(str(stage.input_key)) # Set the input key
                stage_editor_panel.input_properties_editor.special_case_edit.setText(str(stage.special_case)) # Set the special case
                stage_editor_panel.input_properties_editor.special_case_next_chapter_id_edit.setText(str(stage.special_case_next_chapter_id)) # Set the special case next chapter ID

                print("Stage ID:", stage.stage_id)  # Debug print
                print("Stage Choices:", stage.choices)  # Debug print
                print(f"Debug: Stage ID: {stage.stage_id}, Choices: {stage.choices}")  # Debug print

                # Handling choices for input stage
                for choice in stage.choices: # Loop through the choices
                    stage_editor_panel.input_properties_editor.add_choice(choice.text, choice.next_chapter_id) # Add the choice to the input stage

            # Add stage_editor_panel to the view
            self.view.stage_editor_container.addWidget(stage_editor_panel) # Add the stage editor panel to the stage editor container

            # Add a separator line
            separator = QFrame() # Create a separator
            separator.setFrameShape(QFrame.HLine) # Set the frame shape to horizontal line
            separator.setFrameShadow(QFrame.Sunken) # Set the frame shadow to sunken
            separator.setFixedHeight(2)  # Set a fixed height for the separator
            self.view.stage_editor_container.addWidget(separator) # Add the separator to the stage editor container
