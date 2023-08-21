import logging
import sys
from PyQt5.QtWidgets import QApplication
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController
from utils import apply_dark_mode, center_on_screen, configure_logging

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