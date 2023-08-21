import logging
import sys
from PyQt5.QtWidgets import QApplication
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController
from utils import apply_dark_mode, center_on_screen, configure_logging

def main(): # Main function
    configure_logging() # Configure logging
    logging.info("Application started") # Log application start

    try: # Try to run the application
        app = QApplication(sys.argv) # Create the application
        apply_dark_mode(app) # Apply dark mode
        controller = MainMenuController(None)  # Create controller first
        view = MainMenuView(controller)  # Pass the controller to the view
        controller.view = view  # Assign view to controller
        view.resize(1280, 780) # Resize the view
        center_on_screen(view) # Center the view on the screen
        sys.exit(app.exec_()) # Run the application
    except Exception as e: # Catch any exceptions
        print(f"An error occurred: {e}") # Print the error
        sys.exit(1) # Exit the application with error code 1

if __name__ == "__main__": # If the file is run directly
    main() # Run the main function