# views/Lobby.py
# the waiting lobby for users to enter before the game begins

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import asyncio
import websockets

class Lobby(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.players = 0 # By default 0 players :(

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title
        self.title = QLabel("Lobby - Waiting for more players to join!")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.title)

        # Player count label (how many clients have joined)
        self.player_count_label = QLabel(f"Players in lobby: {self.players}")
        self.layout.addWidget(self.player_count_label)
        
        # Start game button
        self.start_button = QPushButton("Start Game")
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

    def set_player_count(self, count):
        # Adds 1 player for each new joined client
        self.players = count
        self.player_count_label.setText(f"Players in lobby: {self.players}")

    def start_game(self):
        print("Game is starting! with deck __")
        self.app.go_to_quiz_player(self.app.deck)

    def update_ui(self):
        if self.app.isHost:
            self.start_button.show()
        else:
            self.start_button.hide()

