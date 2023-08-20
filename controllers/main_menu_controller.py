from views.writer_view import WriterView
from controllers.writer_view_controller import WriterViewController

class MainMenuController:
    def __init__(self): # Accept parent window
        self.view = None  # Initialize view as None; it will be assigned later

    def create_new_chapter(self): # This method will be called when the user clicks the "Create New Chapter" button
        # Open the WriterView for creating a new chapter
        writer_view_controller = WriterViewController(None) # Pass None as parent
        writer_view = WriterView(writer_view_controller) # Pass the controller to the view
        writer_view_controller.view = writer_view # Pass the view to the controller
        self.view.hide()  # Optionally hide the main menu view

    def load_existing_chapter(self):
        # TODO: Prompt the user to select a .json chapter file
        # TODO: Load the selected chapter

        # Open the WriterView with the loaded chapter
        writer_view_controller = WriterViewController(None) # Pass None as parent
        writer_view = WriterView(writer_view_controller) # Pass the controller to the view
        writer_view_controller.view = writer_view # Pass the view to the controller
        self.view.hide()  # Optionally hide the main menu view
