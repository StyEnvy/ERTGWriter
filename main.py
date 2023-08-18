import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtGui import QPalette, QColor
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController

def apply_dark_mode(app):
    # Dark Mode Theme
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    app.setPalette(palette)

def center_on_screen(window):
    # Center the window on the primary screen
    center_point = QDesktopWidget().availableGeometry().center()
    frame_geometry = window.frameGeometry()
    frame_geometry.moveCenter(center_point)
    window.move(frame_geometry.topLeft())

def main():
    # Set up logging
    # (Add logging configuration here if needed)

    try:
        app = QApplication(sys.argv)
        apply_dark_mode(app) # Apply dark mode theme
        controller = MainMenuController()
        view = MainMenuView(controller)
        view.resize(1280, 780) # Set default window size
        center_on_screen(view) # Center the window on the primary screen
        controller.view = view
        sys.exit(app.exec_())
    except Exception as e:
        # Handle exceptions
        # (Log the exception here and provide user-friendly error messages if needed)
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
