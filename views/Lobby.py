# views/Lobby.py
# the waiting lobby for users to enter before the game begins

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
import asyncio
import websockets

class Lobby(QWidget):
    def __init__(self, app):
        super().__init__()

        layout = QVBoxLayout()

        # Title
        title = QLabel("Lobby - Waiting for more players to join!")
        title.setStyleSheet("font-size: 24px; fornt-weight: bold;")
        layout.addWidget(title)

