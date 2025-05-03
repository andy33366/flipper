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

        # Button to attempt to join game (hardcoded rn for testing)
        join_button = QPushButton("Join Game")
        join_button.clicked.connect(lambda: (self.app.go_to_lobby(), self.app.start_client()))
        layout.addWidget(join_button)

        self.setLayout(layout)
