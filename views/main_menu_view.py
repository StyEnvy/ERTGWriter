from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class MainMenuView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Main layout
        main_layout = QVBoxLayout()

        # Title layout (to stack title and subtitle)
        title_layout = QVBoxLayout()
        title_layout.setSpacing(0)  # No space between title and subtitle

        # Title
        title_label = QLabel("ERTG Writer")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: white;")
        title_layout.addWidget(title_label)

        # Subtitle
        subtitle_label = QLabel("This is a proprietary tool for Erainor RPG.")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("font-size: 18px; color: white;")
        title_layout.addWidget(subtitle_label)

        main_layout.addLayout(title_layout)

        # Buttons layout
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(5)  # Reduce space between buttons

        # Create New Chapter Button
        self.new_chapter_button = QPushButton("Create New Chapter")
        self.new_chapter_button.clicked.connect(self.controller.create_new_chapter)
        self.new_chapter_button.setFixedSize(200, 50)
        self.new_chapter_button.setStyleSheet("padding: 10px; font-size: 16px; color: black;")
        buttons_layout.addWidget(self.new_chapter_button, alignment=Qt.AlignCenter)

        # Load Existing Chapter Button
        self.load_chapter_button = QPushButton("Load Existing Chapter")
        self.load_chapter_button.clicked.connect(self.controller.load_existing_chapter)
        self.load_chapter_button.setFixedSize(200, 50)
        self.load_chapter_button.setStyleSheet("padding: 10px; font-size: 16px; color: black;")
        buttons_layout.addWidget(self.load_chapter_button, alignment=Qt.AlignCenter)

        main_layout.addLayout(buttons_layout)

        # Copyright Label
        copyright_label = QLabel("© 2023 Envy Games - For use with Erainor RPG.")
        copyright_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        copyright_label.setStyleSheet("font-size: 12px; color: gray;")
        main_layout.addWidget(copyright_label)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("ERTG Writer")

        self.show()
