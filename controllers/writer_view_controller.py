from models.chapter import LinearStage, InputStage, Choice, Chapter
from views.about_dialog import AboutDialog
from views.documentation_view import DocumentationView
from controllers.documentation_view_controller import DocumentationViewController
from views.stage_editor_panel import StageEditorPanel
from PyQt5.QtWidgets import QFrame
import json

class WriterViewController:
    def __init__(self, view, file_path=None):
        self.view = view
        self.current_chapter = None
        if file_path:
            self.parse_and_load_chapter(file_path)

    def new_chapter(self):
        # Logic for creating a new chapter
        pass

    def open_chapter(self):
        # Logic for opening an existing chapter
        pass

    def save_chapter(self):
        # Logic for saving the current chapter
        pass

    def export_json(self):
        # Logic for exporting the chapter to a JSON file
        pass

    def about(self):
        about_dialog = AboutDialog() # Create an instance of the AboutDialog class
        about_dialog.exec_() # Show the AboutDialog

    def documentation(self):
        self.documentation_controller = DocumentationViewController(view=None) # Create controller without view
        self.documentation_view = DocumentationView(controller=self.documentation_controller, parent=self.view) # Create view with controller
        self.documentation_controller.view = self.documentation_view # Assign view to controller
        self.documentation_view.show() # Show the DocumentationView

    def parse_and_load_chapter(self, file_path: str):
        json_data = self.load_chapter_from_file(file_path)
        chapter = self.parse_chapter(json_data)
        self.current_chapter = chapter
        print(chapter)  # Print the loaded chapter to verify it's loaded correctly
        self.update_gui_with_chapter(chapter, file_path)  # Call method to update GUI with file_path

    def update_gui_with_chapter(self, chapter, file_path: str):
        chapter_id = file_path.split("_")[-1].split(".")[0]  # Extract chapter ID from file path
        self.view.chapter_info_panel.chapter_id_edit.setText(chapter_id)

        # Clear existing stages
        for _ in range(self.view.stage_editor_container.count()):
            widget = self.view.stage_editor_container.itemAt(0).widget()
            if widget:
                widget.deleteLater()

        # Add loaded stages to StageEditorContainer
        for stage in chapter.stages:
            stage_editor_panel = StageEditorPanel()

            # Set the stage ID
            stage_editor_panel.stage_id_edit.setText(str(stage.stage_id))

            # Set the stage text
            stage_editor_panel.stage_text_editor.setText(stage.text)

            # Set the stage type and properties
            if isinstance(stage, LinearStage):
                stage_editor_panel.stage_type_selector.setCurrentIndex(0)
                stage_editor_panel.linear_properties_editor.next_stage_id_edit.setText(str(stage.next_stage_id))
            elif isinstance(stage, InputStage):
                stage_editor_panel.stage_type_selector.setCurrentIndex(1)
                stage_editor_panel.input_properties_editor.next_stage_id_edit.setText(str(stage.next_stage_id))
                stage_editor_panel.input_properties_editor.input_key_edit.setText(str(stage.input_key))
                # Add other properties as needed

            # Add stage_editor_panel to the view
            self.view.stage_editor_container.addWidget(stage_editor_panel)

            # Add a separator line
            separator = QFrame()
            separator.setFrameShape(QFrame.HLine)
            separator.setFrameShadow(QFrame.Sunken)
            separator.setFixedHeight(2)  # Set a fixed height for the separator
            self.view.stage_editor_container.addWidget(separator)

    def parse_chapter(self, json_data: dict) -> Chapter:
        stages = []
        for stage_data in json_data['stages']:
            stage_id = stage_data['id']
            text = stage_data['text']
            properties = stage_data['properties']
            stage_type = properties['type']
            next_stage_id = properties.get('next_stage_id')
            if stage_type == 'linear':
                stage = LinearStage(stage_id, text, next_stage_id)
            else:
                input_key = properties['input_key']
                special_case = properties.get('special_case')
                special_case_next_chapter_id = properties.get('special_case_next_chapter_id')
                choices_data = properties.get('choices', [])
                choices = [Choice(choice['text'], choice['next_chapter_id']) for choice in choices_data]
                stage = InputStage(stage_id, text, input_key, next_stage_id, special_case,
                                   special_case_next_chapter_id, choices)
            stages.append(stage)
        return Chapter(stages)

    def load_chapter_from_file(self, file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)
