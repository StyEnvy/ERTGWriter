from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea 
from PyQt5.QtGui import QPalette, QColor
from views.chapter_information_panel import ChapterInformationPanel
from views.stage_editor_panel import StageEditorPanel

class WriterView(QMainWindow):
    def __init__(self, controller): # Accept parent window
        super().__init__() # Call the parent QMainWindow constructor
        self.controller = controller # Store the controller

        # Dark Mode Theme for Menu Bar
        palette = QPalette() # Create a palette
        palette.setColor(QPalette.Window, QColor(53, 53, 53)) # Set the window color
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255)) # Set the window text color
        palette.setColor(QPalette.Text, QColor(255, 255, 255)) # Set the text color
        self.setPalette(palette) # Apply the palette to the application
        
        # Menu Bar
        menu_bar = self.menuBar() # Create a menu bar
        menu_bar.setStyleSheet("background-color: #353535; color: white;") # Set the menu bar style

        # File Menu
        file_menu = menu_bar.addMenu('File') # Create a file menu
        file_menu.addAction('New Chapter', self.controller.new_chapter) # Add actions to the file menu
        file_menu.addAction('Open Chapter', self.controller.open_chapter) # Add actions to the file menu
        file_menu.addAction('Save Chapter', self.controller.save_chapter) # Add actions to the file menu
        file_menu.addAction('Export JSON', self.controller.export_json) # Add actions to the file menu

        # Help Menu
        help_menu = menu_bar.addMenu('Help') # Create a help menu
        help_menu.addAction('About', self.controller.about) # Add actions to the help menu
        help_menu.addAction('Documentation', self.controller.documentation)

        # Main Layout (Vertical)
        main_layout = QVBoxLayout()

        # Chapter Information Panel (Top)
        self.chapter_info_panel = ChapterInformationPanel()
        main_layout.addWidget(self.chapter_info_panel)

        # Stage Editor Panel (Middle) - Wrapped in a Scroll Area for dynamic sizing
        self.stage_editor_scroll_area = QScrollArea()
        self.stage_editor_panel = StageEditorPanel()
        self.stage_editor_scroll_area.setWidget(self.stage_editor_panel)
        self.stage_editor_scroll_area.setWidgetResizable(True)
        main_layout.addWidget(self.stage_editor_scroll_area)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Window Title
        self.setWindowTitle("ERTG - Chapter Writer") # Set the window title

        # Set default window size
        self.resize(1280, 780) # Set default window size

        self.show()
