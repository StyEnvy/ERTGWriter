from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QFrame
from PyQt5.QtGui import QPalette, QColor
from views.chapter_information_panel import ChapterInformationPanel
from views.stage_editor_panel import StageEditorPanel

class WriterView(QMainWindow):
    def __init__(self, controller, new_chapter=True): # controller is the controller to control
        super().__init__() # Call the parent constructor
        self.controller = controller # Set the controller

        self.create_menu_bar() # Create the menu bar
        self.create_main_layout(new_chapter) # Create the main layout

        # Window Title
        self.setWindowTitle("ERTG - Chapter Writer") # Set the window title

        # Set default window size
        self.resize(1280, 780) # Resize the window
        self.show() # Show the window

    def create_menu_bar(self):
        # Dark Mode Theme for Menu Bar
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53)) # Set the window color
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255)) # Set the window text color
        palette.setColor(QPalette.Text, QColor(255, 255, 255)) # Set the text color
        self.setPalette(palette)

        # Menu Bar
        menu_bar = self.menuBar() # Create a menu bar
        menu_bar.setStyleSheet("font-size: 16px; background-color: #353535; color: white;") # Set the menu bar style sheet

        # File Menu
        file_menu = menu_bar.addMenu('File') # Create a file menu
        file_menu.addAction('New Chapter', self.controller.new_chapter) # Add a new chapter action to the file menu
        file_menu.addAction('Open Chapter', self.controller.open_chapter) # Add an open chapter action to the file menu
        file_menu.addAction('Save Chapter', self.controller.save_chapter) # Add a save chapter action to the file menu

        # Help Menu
        help_menu = menu_bar.addMenu('Help') # Create a help menu
        help_menu.addAction('About', self.controller.about)  # Add an about action to the help menu

    def create_main_layout(self, new_chapter): # Function to create the main layout
        # Main Layout (Vertical)
        main_layout = QVBoxLayout() # Create a main layout

        # Top Layout (Horizontal)
        top_layout = QHBoxLayout()

        # Chapter Information Panel (Top Left)
        self.chapter_info_panel = ChapterInformationPanel() # Create a chapter information panel
        top_layout.addWidget(self.chapter_info_panel) # Add the chapter information panel to the top layout

        top_layout.addStretch(1) # Add a stretch to push the button to the right

        # Documentation Button (Top Right)
        documentation_button = QPushButton("Documentation")
        documentation_button.setStyleSheet("font-size: 16px;") # Set the font size
        documentation_button.setFixedWidth(120) # Set a fixed width
        documentation_button.clicked.connect(self.controller.documentation) # Connect the button to the documentation function
        top_layout.addWidget(documentation_button)

        main_layout.addLayout(top_layout) # Add the top layout to the main layout

        # Stage Editor Container (Middle) inside a Scroll Area
        self.stage_editor_container = QVBoxLayout() # Create a stage editor container
        stage_editor_widget = QWidget() # Create a stage editor widget
        stage_editor_widget.setLayout(self.stage_editor_container) # Set the stage editor container layout
        scroll_area = QScrollArea() # Create a scroll area
        scroll_area.setWidget(stage_editor_widget) # Add the stage editor widget to the scroll area
        scroll_area.setWidgetResizable(True) # Allow the scroll area to resize the widget
        main_layout.addWidget(scroll_area) # Add the scroll area to the main layout

        # Add a default stage editor panel if creating a new chapter
        if new_chapter: # If creating a new chapter
            self.add_stage() # Add a stage editor panel

        # Add/Remove Stage Buttons
        stage_buttons_layout = QHBoxLayout() # Create a stage buttons layout
        add_stage_button = QPushButton("Add Stage") # Create an add stage button
        add_stage_button.setStyleSheet("font-size: 16px;") # Set the font size
        add_stage_button.clicked.connect(self.add_stage) # Connect the add stage button to the add stage function
        remove_stage_button = QPushButton("Remove Stage") # Create a remove stage button
        remove_stage_button.setStyleSheet("font-size: 16px;") # Set the font size
        remove_stage_button.clicked.connect(self.remove_stage) # Connect the remove stage button to the remove stage function
        stage_buttons_layout.addWidget(add_stage_button) # Add the stage buttons to the stage buttons layout
        stage_buttons_layout.addWidget(remove_stage_button) # Add the stage buttons to the stage buttons layout
        main_layout.addLayout(stage_buttons_layout) # Add the stage buttons layout to the main layout

        main_widget = QWidget() # Create a main widget
        main_widget.setLayout(main_layout) # Set the main layout
        self.setCentralWidget(main_widget) # Set the main widget

    def add_stage(self):
        stage_editor_panel = StageEditorPanel() # Create a StageEditorPanel
        self.stage_editor_container.addWidget(stage_editor_panel) # Add the stage editor panel to the stage editor container

        # Add a separator line
        separator = QFrame() # Create a separator
        separator.setFrameShape(QFrame.HLine) # Set the frame shape to horizontal line
        separator.setFrameShadow(QFrame.Sunken) # Set the frame shadow to sunken
        separator.setFixedHeight(2)  # Set a fixed height for the separator
        self.stage_editor_container.addWidget(separator) # Add the separator to the stage editor container

    def remove_stage(self):
        if self.stage_editor_container.count() >= 2: # If there are at least 2 widgets in the stage editor container
            stage_editor_panel = self.stage_editor_container.itemAt(self.stage_editor_container.count() - 2).widget() # Get the stage editor panel
            stage_editor_panel.deleteLater() # Delete the stage editor panel
            separator = self.stage_editor_container.itemAt(self.stage_editor_container.count() - 1).widget() # Get the separator
            separator.deleteLater() # Delete the separator