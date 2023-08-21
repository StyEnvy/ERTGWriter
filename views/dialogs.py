from PyQt5.QtWidgets import QMessageBox

class ConfirmNewChapterDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('New Chapter')
        self.setText('Are you sure you want to start a new chapter? Unsaved changes will be lost.')
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setStyleSheet("color: black;")

class InvalidChapterIdDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Invalid Chapter ID')
        self.setText('Please enter a valid chapter ID before saving.')
        self.setStandardButtons(QMessageBox.Ok)
        self.setStyleSheet("color: black;")

class AboutDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About ERTGWriter')
        self.setText('ERTGWriter - A tool for creating and editing chapters for text-based RPGs.\n\nVersion: 1.0\nDeveloped by: YourName')
        self.setStandardButtons(QMessageBox.Ok)
        self.setStyleSheet("color: black;")
