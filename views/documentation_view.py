from PyQt5.QtWidgets import QMainWindow, QListWidget, QTextBrowser, QDockWidget, QWidget
from PyQt5.QtCore import Qt

class DocumentationView(QMainWindow):
    def __init__(self, parent=None):  # Accept parent window
        super().__init__(parent)  # Pass parent to the QMainWindow constructor

        # Table of Contents
        toc_list = QListWidget()
        toc_list.addItem("Introduction")
        toc_list.addItem("Getting Started")
        toc_list.addItem("Chapter Creation")
        toc_list.addItem("Stages")
        # Add more items as needed...

        toc_dock = QDockWidget("Table of Contents", self)
        toc_dock.setWidget(toc_list)
        self.addDockWidget(Qt.LeftDockWidgetArea, toc_dock)

        # Documentation Text
        doc_browser = QTextBrowser()

        central_widget = QWidget()
        self.setCentralWidget(doc_browser)

        self.setWindowTitle("Documentation - ERTG Writer")
