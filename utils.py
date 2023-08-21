import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QPalette, QColor

def apply_dark_mode(app):
    # Dark Mode Theme
    palette = QPalette() # Create a palette
    palette.setColor(QPalette.Window, QColor(53, 53, 53)) # Set the window color
    palette.setColor(QPalette.WindowText, Qt.white) # Set the window text color
    palette.setColor(QPalette.Base, QColor(25, 25, 25)) # Set the base color
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53)) # Set the alternate base color
    palette.setColor(QPalette.Text, Qt.white) # Set the text color
    palette.setColor(QPalette.Button, QColor(53, 53, 53)) # Set the button color
    palette.setColor(QPalette.ButtonText, Qt.black) # Set the button text color
    app.setPalette(palette) # Apply the palette to the application

def center_on_screen(window):
    # Center the window on the primary screen
    center_point = QDesktopWidget().availableGeometry().center() # Get center point of primary screen
    frame_geometry = window.frameGeometry() # Get frame geometry of window
    frame_geometry.moveCenter(center_point) # Move frame geometry to center point
    window.move(frame_geometry.topLeft()) # Move window to top left of frame geometry

def configure_logging():
    logging.basicConfig(
        level=logging.INFO, # Set the logging level to INFO
        format="%(asctime)s [%(levelname)s] %(message)s", # Set the format for log messages
        handlers=[
            logging.FileHandler("application.log"), # Log messages to a file
            logging.StreamHandler() # Print log messages to console
        ]
    )