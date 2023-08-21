from models.chapter import LinearStage, InputStage, Choice, Chapter
from views.about_dialog import AboutDialog
from views.documentation_view import DocumentationView
from controllers.documentation_view_controller import DocumentationViewController
from views.stage_editor_panel import StageEditorPanel
from controllers.file_operations import FileOperations
from PyQt5.QtWidgets import QFrame, QMessageBox, QFileDialog
import json

class WriterViewController:
    def __init__(self, view, file_path=None):
        self.view = view
        self.file_operations = FileOperations()
        self.current_chapter = None
        self.current_file_path = file_path
        if file_path:
            self.parse_and_load_chapter(file_path)

    def new_chapter(self):
        # Create a QMessageBox instance for the confirmation dialog
        confirmation_dialog = QMessageBox(self.view)
        confirmation_dialog.setWindowTitle('New Chapter')
        confirmation_dialog.setText('Are you sure you want to start a new chapter? Unsaved changes will be lost.')
        confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    
        # Set the text color to black
        confirmation_dialog.setStyleSheet("color: black;")
    
        # Show the dialog and get the user's response
        confirmation = confirmation_dialog.exec_()
    
        if confirmation == QMessageBox.Yes:
            # Clear existing stages
            while self.view.stage_editor_container.count() > 0:
                item = self.view.stage_editor_container.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            # Clear chapter ID field
            self.view.chapter_info_panel.chapter_id_edit.clear()

            # Set current chapter to None
            self.current_chapter = None
            print("New chapter started")  # Debug print

            # Clear current file path
            self.current_file_path = None

    def open_chapter(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Open Chapter", "", "Chapter Files (*.json);;All Files (*)", options=options)
        if file_path:
            self.current_file_path = file_path
            # Clear existing stages before loading the new chapter
            for _ in range(self.view.stage_editor_container.count()):
                widget = self.view.stage_editor_container.itemAt(0).widget()
                if widget:
                    widget.deleteLater()

            self.parse_and_load_chapter(file_path)
            print(f"Chapter loaded from {file_path}")  # Debug print

    def save_chapter(self):
        # Check if the current chapter has been saved before
        if self.current_file_path:
            self.save_to_file(self.current_file_path)
        else:
            self.save_chapter_as()

    def save_to_file(self, file_path: str):
        # Logic to save the current chapter to the specified file path
        stages = []
        for index in range(0, self.view.stage_editor_container.count(), 2): # Step by 2 to skip separators
            stage_editor_panel = self.view.stage_editor_container.itemAt(index).widget()
            # Build the stage data from the panel (you'll need to implement this method)
            stage = stage_editor_panel.build_stage()
            stages.append(stage)
        chapter_data = {'stages': stages}
        with open(file_path, 'w') as file:
            json.dump(chapter_data, file, indent=4)
        print(f"Chapter saved to {file_path}")  # Debug print

    def save_chapter_as(self):
        chapter_id = self.view.chapter_info_panel.chapter_id_edit.text().strip()
        if chapter_id.isdigit():
            default_name = f"chapter_{chapter_id}.json"
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self.view, "Save Chapter", default_name, "Chapter Files (*.json);;All Files (*)", options=options)
            if file_path:
                self.current_file_path = file_path
                self.save_to_file(file_path)
        else:
            QMessageBox.warning(self.view, "Invalid Chapter ID", "Please enter a valid chapter ID before saving.")

    def about(self):
        about_dialog = AboutDialog() # Create an instance of the AboutDialog class
        about_dialog.exec_() # Show the AboutDialog

    def documentation(self):
        self.documentation_controller = DocumentationViewController(view=None) # Create controller without view
        self.documentation_view = DocumentationView(controller=self.documentation_controller, parent=self.view) # Create view with controller
        self.documentation_controller.view = self.documentation_view # Assign view to controller
        self.documentation_view.show() # Show the DocumentationView

    def parse_and_load_chapter(self, file_path: str):
        json_data = self.file_operations.load_chapter_from_file(file_path)  # Use the method from FileOperations
        chapter = self.file_operations.parse_chapter(json_data)  # Use the method from FileOperations
        self.current_chapter = chapter
        self.current_file_path = file_path
        print(chapter)
        self.update_gui_with_chapter(chapter, file_path)

    def save_to_file(self, file_path: str):
        self.file_operations.save_to_file(self.view.stage_editor_container, file_path)  # Use the method from FileOperations

    def update_gui_with_chapter(self, chapter, file_path: str):
        chapter_id = file_path.split("_")[-1].split(".")[0]  # Extract chapter ID from file path
        self.view.chapter_info_panel.chapter_id_edit.setText(chapter_id)

        # Clear existing stages
        while self.view.stage_editor_container.count() > 0:
            item = self.view.stage_editor_container.takeAt(0)
            widget = item.widget()
            if widget is not None:
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
                stage_editor_panel.input_properties_editor.special_case_edit.setText(str(stage.special_case))
                stage_editor_panel.input_properties_editor.special_case_next_chapter_id_edit.setText(str(stage.special_case_next_chapter_id))

                print("Stage ID:", stage.stage_id)  # Debug print
                print("Stage Choices:", stage.choices)  # Debug print
                print(f"Debug: Stage ID: {stage.stage_id}, Choices: {stage.choices}")  # Debug print

                # Handling choices for input stage
                for choice in stage.choices:
                    stage_editor_panel.input_properties_editor.add_choice(choice.text, choice.next_chapter_id)

            # Add stage_editor_panel to the view
            self.view.stage_editor_container.addWidget(stage_editor_panel)

            # Add a separator line
            separator = QFrame()
            separator.setFrameShape(QFrame.HLine)
            separator.setFrameShadow(QFrame.Sunken)
            separator.setFixedHeight(2)  # Set a fixed height for the separator
            self.view.stage_editor_container.addWidget(separator)




