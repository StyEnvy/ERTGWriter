from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QColor, QPalette

class WriterView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Dark Mode Theme for Menu Bar
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.setPalette(palette)
        
        # Menu Bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: #353535; color: white;")

        # File Menu
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction('New Chapter', self.controller.new_chapter)
        file_menu.addAction('Open Chapter', self.controller.open_chapter)
        file_menu.addAction('Save Chapter', self.controller.save_chapter)
        file_menu.addAction('Export JSON', self.controller.export_json)
        file_menu.addSeparator()
        file_menu.addAction('Exit', self.controller.exit)

        # Edit Menu
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Undo', self.controller.undo)
        edit_menu.addAction('Redo', self.controller.redo)
        edit_menu.addAction('Copy', self.controller.copy)
        edit_menu.addAction('Paste', self.controller.paste)
        edit_menu.addAction('Delete', self.controller.delete)

        # Help Menu
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction('About', self.controller.about)
        help_menu.addAction('Documentation', self.controller.documentation)
        # Window Title
        self.setWindowTitle("ERTG - Chapter Writer")

        # Set default window size
        self.resize(1280, 780)

        # Other initialization code here...

        self.show()
