# views/GameSelection
# The menu where the ****CLIENT**** user will enter an IP address/port to join a hosted game

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

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

        # Text boxes for entering IP addr and port
        self.host_game_input = QLineEdit()
        self.host_game_input.setPlaceholderText("Enter the IP address of the host")
        layout.addWidget(self.host_game_input)

        # Go to lobby

        self.setLayout(layout)
