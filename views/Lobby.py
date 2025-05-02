# views/Lobby.py
# the waiting lobby for users to enter before the game begins

from PyQt6.QtWidgets import Qwidget, QVBoxLayout, QPushButton, QLabel
import asyncio
import websockets

class Lobby(QWidget):
    def __init__(self, app, arg):
        super().__init__()

        layout = QVBoxLayout()

        # Title
        title = QLabel("Lobby - Waiting for more players to join!")
        title.setStyleSheet("font-size: 24px; fornt-weight: bold;")
        layout.addWidget(title)

        # For testing : add a txt box where user can send txt to the server, see if the server returns the message
