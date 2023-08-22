from PyQt5.QtWidgets import QMainWindow, QListWidget, QTextBrowser, QDockWidget, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class CustomDockWidget(QDockWidget): # This class inherits from QDockWidget
    def __init__(self, title, parent=None): # Accept parent window
        super().__init__(title, parent) # Call the parent QDockWidget constructor
        self.initTitleBar() # Call the method to initialize the title bar

    def initTitleBar(self): # This method is called from the constructor
        title_bar = QWidget() # Create a widget for the title bar
        layout = QHBoxLayout() # Create a layout for the title bar widget
        layout.setContentsMargins(0, 0, 0, 0) # Set the layout margins to 0

        title_label = QLabel(self.windowTitle()) # Create a title label
        close_button = QPushButton("X") # Create a close button
        close_button.setStyleSheet("font-size: 16px; color: white; background: #333;") # Set the button text and background color

        close_button.clicked.connect(self.close) # Connect the close button to the close method

        layout.addWidget(title_label) # Add the title label to the layout
        layout.addStretch() # Add a stretch to push the close button to the right
        layout.addWidget(close_button) # Add the close button to the layout

        title_bar.setLayout(layout) # Set the layout for the title bar widget
        self.setTitleBarWidget(title_bar) # Set the title bar widget

class DocumentationView(QMainWindow): 
    def __init__(self, controller, parent=None): # Accept parent window
        super().__init__(parent) # Call the parent QMainWindow constructor
        self.controller = controller # Store the controller

        # Table of Contents
        toc_list = QListWidget() # Make it an instance variable
        toc_list.setStyleSheet("font-size: 16px;")
        toc_list.addItem("Introduction") # Add items to the list
        toc_list.addItem("Getting Started")
        toc_list.addItem("Basic Chapter Explanation")
        toc_list.addItem("Stage Type Explanation")
        toc_list.addItem("Character Attributes")
        toc_list.addItem("Building a Chapter")
        toc_list.addItem("Saving a Chapter")

        toc_dock = CustomDockWidget("Table of Contents", self) # Create a custom dock widget
        toc_dock.setWidget(toc_list) # Set the list widget as the dock widget
        self.addDockWidget(Qt.LeftDockWidgetArea, toc_dock) # Add the dock widget to the main window

        toc_list.itemClicked.connect(self.controller.load_content) # Connect to the controller method

        # Documentation Text
        self.doc_browser = QTextBrowser() # Make it an instance variable

        central_widget = QWidget()
        self.setCentralWidget(self.doc_browser) # Set the text browser as the central widget

        self.setWindowTitle("Documentation - ERTG Writer") # Set the window title
