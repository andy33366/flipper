# views/GameSelection
# The menu where the ****CLIENT**** user will enter an IP address/port to join a hosted game

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class GameSelection(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app # Reference to the FlipperApp
        self.app.isMultiPlayer = True
        self.app.isHost = False

        layout = QVBoxLayout()

        # Title label
        title = QLabel("Game Selection")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.setLayout(layout)
