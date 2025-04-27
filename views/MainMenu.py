# views/MainMenu.py
# The main menu interface to choose between functions

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class MainMenu(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app  # Reference to the FlipperApp

        layout = QVBoxLayout()

        # Title label
        title = QLabel("Welcome to Flipper")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Button to go to deck builder
        build_button = QPushButton("Build a Deck")
        build_button.clicked.connect(self.app.go_to_deck_builder)
        layout.addWidget(build_button)

        # Button to go to quiz (you'd load real decks in a real app)
        quiz_button = QPushButton("Take a Quiz")
        quiz_button.clicked.connect(self.app.go_to_deck_selection)
        layout.addWidget(quiz_button)

        self.setLayout(layout)
