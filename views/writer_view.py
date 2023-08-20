from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QFrame
from PyQt5.QtGui import QPalette, QColor
from views.chapter_information_panel import ChapterInformationPanel
from views.stage_editor_panel import StageEditorPanel

class WriterView(QMainWindow):
    def __init__(self, controller, new_chapter=True):
        super().__init__()
        self.controller = controller

        # Dark Mode Theme for Menu Bar
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        self.setPalette(palette)

        # Menu Bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: #353535; color: white;")

        # File Menu
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction('New Chapter', self.controller.new_chapter)
        file_menu.addAction('Open Chapter', self.controller.open_chapter)
        file_menu.addAction('Save Chapter', self.controller.save_chapter)
        file_menu.addAction('Export JSON', self.controller.export_json)

        # Help Menu
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction('About', self.controller.about)
        help_menu.addAction('Documentation', self.controller.documentation)

        # Main Layout (Vertical)
        main_layout = QVBoxLayout()

        # Chapter Information Panel (Top)
        self.chapter_info_panel = ChapterInformationPanel()
        main_layout.addWidget(self.chapter_info_panel)

        # Stage Editor Container (Middle) inside a Scroll Area
        self.stage_editor_container = QVBoxLayout()
        stage_editor_widget = QWidget()
        stage_editor_widget.setLayout(self.stage_editor_container)
        scroll_area = QScrollArea()
        scroll_area.setWidget(stage_editor_widget)
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Add a default stage editor panel if creating a new chapter
        if new_chapter:
            self.add_stage()

        # Add/Remove Stage Buttons
        stage_buttons_layout = QHBoxLayout()
        add_stage_button = QPushButton("Add Stage")
        add_stage_button.clicked.connect(self.add_stage)
        remove_stage_button = QPushButton("Remove Stage")
        remove_stage_button.clicked.connect(self.remove_stage)
        stage_buttons_layout.addWidget(add_stage_button)
        stage_buttons_layout.addWidget(remove_stage_button)
        main_layout.addLayout(stage_buttons_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Window Title
        self.setWindowTitle("ERTG - Chapter Writer")

        # Set default window size
        self.resize(1280, 780)
        self.show()

    def add_stage(self):
        stage_editor_panel = StageEditorPanel()
        self.stage_editor_container.addWidget(stage_editor_panel)

        # Add a separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setFixedHeight(2)  # Set a fixed height for the separator
        self.stage_editor_container.addWidget(separator)

    def remove_stage(self):
        if self.stage_editor_container.count() >= 2:
            stage_editor_panel = self.stage_editor_container.itemAt(self.stage_editor_container.count() - 2).widget()
            stage_editor_panel.deleteLater()
            separator = self.stage_editor_container.itemAt(self.stage_editor_container.count() - 1).widget()
            separator.deleteLater()