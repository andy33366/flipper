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

        # Button to host a multiplayer game
        host_button = QPushButton("Start a Game")
        #sets multiplayer to true and goes to deck selection screen
        host_button.clicked.connect(lambda: (self.app.set_multiplayer(True), self.app.go_to_deck_selection()))
        layout.addWidget(host_button)

        # BUtton to join a multiplayer game
        join_button = QPushButton("Join a Game")
        #TO DO : make go_to_game_selection
        join_button.clicked.connect(self.app.go_to_game_selection)
        layout.addWidget(join_button)


        self.setLayout(layout)
