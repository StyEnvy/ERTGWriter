from PyQt5.QtWidgets import QFileDialog
from views.writer_view import WriterView
from controllers.writer_view_controller import WriterViewController

class MainMenuController:
    def __init__(self, view):
        self.view = view

    def create_new_chapter(self):
        writer_view_controller = WriterViewController(None) # No need to pass new_chapter
        writer_view = WriterView(writer_view_controller, new_chapter=True)
        writer_view_controller.view = writer_view
        self.view.hide()

    def load_existing_chapter(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Open Chapter", "", "Chapter Files (*.json);;All Files (*)", options=options)
        if file_path:
            writer_view_controller = WriterViewController(view=None)
            writer_view = WriterView(writer_view_controller)  # new_chapter=False by default
            writer_view_controller.view = writer_view
            writer_view.show()
            writer_view_controller.parse_and_load_chapter(file_path)  # Move this line after setting the view
            self.view.hide()




