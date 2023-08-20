import logging
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtGui import QPalette, QColor
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController

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

def main():
    configure_logging()
    logging.info("Application started")

    try:
        app = QApplication(sys.argv)
        apply_dark_mode(app)
        controller = MainMenuController(None)  # Create controller first
        view = MainMenuView(controller)  # Pass the controller to the view
        controller.view = view  # Assign view to controller
        view.resize(1280, 780)
        center_on_screen(view)
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__": 
    main()
