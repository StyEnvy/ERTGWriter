from PyQt5.QtWidgets import QFileDialog
from views.writer_view import WriterView
from controllers.writer_view_controller import WriterViewController

class MainMenuController:
    def __init__(self, view):
        self.view = view

    def create_new_chapter(self): # Function to create a new chapter
        writer_view_controller = WriterViewController(None) # No need to pass new_chapter
        writer_view = WriterView(writer_view_controller, new_chapter=True) # new_chapter=True
        writer_view_controller.view = writer_view # Set the view
        self.view.hide() # Hide the main menu

    def load_existing_chapter(self): # Function to load an existing chapter
        options = QFileDialog.Options() # Create options for the file dialog
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Open Chapter", "", "Chapter Files (*.json);;All Files (*)", options=options) # Open the file dialog
        if file_path: # If a file path was selected
            writer_view_controller = WriterViewController(view=None) # Create a WriterViewController
            writer_view = WriterView(writer_view_controller)  # new_chapter=False by default
            writer_view_controller.view = writer_view # Set the view
            writer_view.show() # Show the view
            writer_view_controller.parse_and_load_chapter(file_path)  # Move this line after setting the view
            self.view.hide() # Hide the main menu




