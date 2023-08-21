from views.dialogs import ConfirmNewChapterDialog, InvalidChapterIdDialog, AboutDialog
from views.documentation_view import DocumentationView
from controllers.documentation_view_controller import DocumentationViewController
from controllers.chapter_gui_update import ChapterGUIUpdater
from controllers.file_operations import FileOperations
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class WriterViewController:
    def __init__(self, view, file_path=None): # view is the view to control
        self.view = view # file_path is the path to the chapter file to load
        self.file_operations = FileOperations() # Create a FileOperations object
        self.current_chapter = None # Create a current_chapter attribute
        self.current_file_path = file_path # Create a current_file_path attribute
        self.chapter_gui_updater = ChapterGUIUpdater(view) # Create a ChapterGUIUpdater object
        if file_path: # If a file path was passed
            self.parse_and_load_chapter(file_path) # Parse and load the chapter

    def new_chapter(self): # Function to start a new chapter
        confirmation_dialog = ConfirmNewChapterDialog(self.view) # Create a confirmation dialog
        confirmation = confirmation_dialog.exec_() # Execute the dialog
        if confirmation == QMessageBox.Yes: # If the user confirmed
            # Clear existing stages # Clear existing stages
            while self.view.stage_editor_container.count() > 0: # Clear existing stages
                item = self.view.stage_editor_container.takeAt(0) # Clear existing stages
                widget = item.widget() # Clear existing stages
                if widget is not None: # Clear existing stages
                    widget.deleteLater() # Clear existing stages

            # Clear chapter ID field
            self.view.chapter_info_panel.chapter_id_edit.clear() # Clear chapter ID field

            # Set current chapter to None
            self.current_chapter = None 
            print("New chapter started")  # Debug print

            # Clear current file path
            self.current_file_path = None

    def open_chapter(self): # Function to open a chapter
        options = QFileDialog.Options() # Create options for the file dialog
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Open Chapter", "", "Chapter Files (*.json);;All Files (*)", options=options) # Open the file dialog
        if file_path: # If a file path was selected
            self.current_file_path = file_path # Set the current file path
            # Clear existing stages before loading the new chapter
            for _ in range(self.view.stage_editor_container.count()): 
                widget = self.view.stage_editor_container.itemAt(0).widget() 
                if widget:
                    widget.deleteLater() 

            self.parse_and_load_chapter(file_path) # Parse and load the chapter
            print(f"Chapter loaded from {file_path}")  # Debug print

    def save_chapter(self): # Function to save the current chapter
        # Check if the current chapter has been saved before
        if self.current_file_path: 
            self.save_to_file(self.current_file_path) # Save the chapter to the current file path
        else: # If the current chapter has not been saved before
            self.save_chapter_as() # Save the chapter as a new file

    def save_chapter_as(self): # Function to save the current chapter as a new file
        chapter_id = self.view.chapter_info_panel.chapter_id_edit.text().strip() # Get the chapter ID
        if chapter_id.isdigit(): # If the chapter ID is a number
            default_name = f"chapter_{chapter_id}.json" # Set the default file name
            options = QFileDialog.Options() # Create options for the file dialog
            file_path, _ = QFileDialog.getSaveFileName(self.view, "Save Chapter", default_name, "Chapter Files (*.json);;All Files (*)", options=options) # Open the file dialog
            if file_path: # If a file path was selected
                self.current_file_path = file_path # Set the current file path
                self.save_to_file(file_path) # Save the chapter to the current file path
        else: # If the chapter ID is not a number
            invalid_chapter_id_dialog = InvalidChapterIdDialog(self.view) # Create an invalid chapter ID dialog
            invalid_chapter_id_dialog.exec_() # Execute the dialog

    def about(self): # Function to show the about dialog
        about_dialog = AboutDialog() # Create an about dialog
        about_dialog.exec_() # Execute the dialog

    def documentation(self): # Function to show the documentation
        self.documentation_controller = DocumentationViewController(view=None) # Create a DocumentationViewController
        self.documentation_view = DocumentationView(controller=self.documentation_controller, parent=self.view) # Create a DocumentationView
        self.documentation_controller.view = self.documentation_view # Assign the view to the controller
        self.documentation_view.show() # Show the view

    def parse_and_load_chapter(self, file_path: str): # Function to parse and load a chapter
        json_data = self.file_operations.load_chapter_from_file(file_path) # Load the chapter from the file
        chapter = self.file_operations.parse_chapter(json_data) # Parse the chapter
        self.current_chapter = chapter # Set the current chapter
        self.current_file_path = file_path # Set the current file path
        print(chapter) # Debug print
        self.chapter_gui_updater.view = self.view  # Update view inside ChapterGUIUpdater
        self.chapter_gui_updater.update_gui_with_chapter(chapter, file_path) # Update the GUI with the chapter

    def save_to_file(self, file_path: str): # Function to save the chapter to a file
        self.file_operations.save_to_file(self.view.stage_editor_container, file_path) # Save the chapter to the file