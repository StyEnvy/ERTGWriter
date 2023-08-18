from views.about_dialog import AboutDialog  # Import the AboutDialog class
from views.documentation_view import DocumentationView # Import the DocumentationView class

class WriterViewController:
    def __init__(self, view):
        self.view = view
        self.documentation_view = None  # Add this line to keep a reference

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

    def exit(self):
        # Logic for exiting the application
        pass

    def undo(self):
        # Logic for undoing the last action
        pass

    def redo(self):
        # Logic for redoing the last undone action
        pass

    def copy(self):
        # Logic for copying the selected content
        pass

    def paste(self):
        # Logic for pasting the copied content
        pass

    def delete(self):
        # Logic for deleting the selected content
        pass

    def about(self):
        about_dialog = AboutDialog() # Create an instance of the AboutDialog class
        about_dialog.exec_() # Show the AboutDialog

    def documentation(self):
        self.documentation_view = DocumentationView(self.view)  # Pass main window as parent
        self.documentation_view.show()

    # Add more methods as needed...
