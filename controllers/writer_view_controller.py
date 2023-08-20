from views.about_dialog import AboutDialog  # Import the AboutDialog class
from views.documentation_view import DocumentationView # Import the DocumentationView class
from controllers.documentation_view_controller import DocumentationViewController # Import the DocumentationViewController class

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

    def about(self):
        about_dialog = AboutDialog() # Create an instance of the AboutDialog class
        about_dialog.exec_() # Show the AboutDialog

    def documentation(self):
        self.documentation_controller = DocumentationViewController(view=None) # Create controller without view
        self.documentation_view = DocumentationView(controller=self.documentation_controller, parent=self.view) # Create view with controller
        self.documentation_controller.view = self.documentation_view # Assign view to controller
        self.documentation_view.show() # Show the DocumentationView

    # Add more methods as needed...
