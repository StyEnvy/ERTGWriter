from views.dialogs import ConfirmNewChapterDialog, InvalidChapterIdDialog, AboutDialog
from views.documentation_view import DocumentationView
from controllers.documentation_view_controller import DocumentationViewController
from controllers.chapter_gui_update import ChapterGUIUpdater
from controllers.file_operations import FileOperations
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class WriterViewController:
    def __init__(self, view, file_path=None):
        self.view = view
        self.file_operations = FileOperations()
        self.current_chapter = None
        self.current_file_path = file_path
        self.chapter_gui_updater = ChapterGUIUpdater(view)  
        if file_path:
            self.parse_and_load_chapter(file_path)

    def new_chapter(self):
        confirmation_dialog = ConfirmNewChapterDialog(self.view)
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
            invalid_chapter_id_dialog = InvalidChapterIdDialog(self.view)
            invalid_chapter_id_dialog.exec_()

    def about(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

    def documentation(self):
        self.documentation_controller = DocumentationViewController(view=None)
        self.documentation_view = DocumentationView(controller=self.documentation_controller, parent=self.view)
        self.documentation_controller.view = self.documentation_view
        self.documentation_view.show()

    def parse_and_load_chapter(self, file_path: str):
        json_data = self.file_operations.load_chapter_from_file(file_path)
        chapter = self.file_operations.parse_chapter(json_data)
        self.current_chapter = chapter
        self.current_file_path = file_path
        print(chapter)
        self.chapter_gui_updater.view = self.view  # Update view inside ChapterGUIUpdater
        self.chapter_gui_updater.update_gui_with_chapter(chapter, file_path)

    def save_to_file(self, file_path: str):
        self.file_operations.save_to_file(self.view.stage_editor_container, file_path)