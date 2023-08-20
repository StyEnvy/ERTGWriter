from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class MainMenuView(QMainWindow):
    def __init__(self, controller): # Accept parent window
        super().__init__() # Call the parent QMainWindow constructor
        self.controller = controller # Store the controller

        # Main layout
        main_layout = QVBoxLayout() # Create a layout for the main window

        # Title layout (to stack title and subtitle)
        title_layout = QVBoxLayout() # Create a layout for the title
        title_layout.setSpacing(0)  # No space between title and subtitle

        # Title
        title_label = QLabel("ERTG Writer") # Create a label
        title_label.setAlignment(Qt.AlignCenter) # Align the label to the center
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: white;") # Set the label style
        title_layout.addWidget(title_label) # Add the label to the title layout

        # Subtitle
        subtitle_label = QLabel("This is a proprietary tool for Erainor RPG.") # Create a label
        subtitle_label.setAlignment(Qt.AlignCenter) # Align the label to the center
        subtitle_label.setStyleSheet("font-size: 18px; color: white;") # Set the label style
        title_layout.addWidget(subtitle_label) # Add the label to the title layout

        main_layout.addLayout(title_layout) # Add the title layout to the main layout

        # Buttons layout
        buttons_layout = QVBoxLayout() # Create a layout for the buttons
        buttons_layout.setSpacing(5)  # Reduce space between buttons

        # Create New Chapter Button
        self.new_chapter_button = QPushButton("Create New Chapter") # Create a button
        self.new_chapter_button.clicked.connect(self.controller.create_new_chapter) # Connect the button to the controller
        self.new_chapter_button.setFixedSize(200, 50) # Set the button size
        self.new_chapter_button.setStyleSheet("padding: 10px; font-size: 16px; color: black;") # Set the button style
        buttons_layout.addWidget(self.new_chapter_button, alignment=Qt.AlignCenter)# Add the button to the buttons layout

        # Load Existing Chapter Button
        self.load_chapter_button = QPushButton("Load Existing Chapter") # Create a button
        self.load_chapter_button.clicked.connect(self.controller.load_existing_chapter) # Connect the button to the controller
        self.load_chapter_button.setFixedSize(200, 50) # Set the button size
        self.load_chapter_button.setStyleSheet("padding: 10px; font-size: 16px; color: black;") # Set the button style
        buttons_layout.addWidget(self.load_chapter_button, alignment=Qt.AlignCenter) # Add the button to the buttons layout

        main_layout.addLayout(buttons_layout) # Add the buttons layout to the main layout

        # Copyright Label
        copyright_label = QLabel("© 2023 Envy Games - For use with Erainor RPG.") # Create a label
        copyright_label.setAlignment(Qt.AlignRight | Qt.AlignBottom) # Align
        copyright_label.setStyleSheet("font-size: 12px; color: gray;") # Set the label style
        main_layout.addWidget(copyright_label) # Add the label to the main layout

        # Set the main layout
        central_widget = QWidget() # Create a central widget
        central_widget.setLayout(main_layout) # Set the main layout for the central widget
        self.setCentralWidget(central_widget) # Set the central widget for the main window
        self.setWindowTitle("ERTG Writer") # Set the window title

        self.show() # Show the main window
