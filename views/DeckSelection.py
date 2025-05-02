# views/DeckSelection.py
# Allows users to select a saved deck to study

import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from models.Card import Deck

class DeckSelection(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.layout = QVBoxLayout()
        self.label = QLabel("Select a Deck to Study:")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def refresh_decks(self):
        #load deck files and create buttons
        # Clear previous buttons
        while self.layout.count() > 1:
            child = self.layout.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

				#if deck does not exist, make it
        deck_dir = "decks"
        if not os.path.exists(deck_dir):
            os.makedirs(deck_dir)

				#grabs the names of all json files (all decks)
        files = [f for f in os.listdir(deck_dir) if f.endswith(".json")]

				#if nothing in files tell user there are no saved decks
        if not files:
            no_decks_label = QLabel("No decks found. Please create one first!")
            self.layout.addWidget(no_decks_label)
            return

				#create buttons for each file
        for filename in files:
            deck_name = filename[:-5]  # Remove '.json' from name
            btn = QPushButton(deck_name)
            #lambda (quick anonymous function) grabs filename once clicked
            btn.clicked.connect(lambda checked, f=filename: self.load_deck(f))
            self.layout.addWidget(btn)

	#loads deck and goes to quiz player or host lobby based on isMultiPlayer variable 
    def load_deck(self, filename):
        try:
            deck = Deck.load_from_file(filename)
            if self.app.isMultiPlayer:
                #goes to the lobby as host
                self.app.go_to_lobby(deck)
            else:
                self.app.go_to_quiz_player(deck)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load deck: {str(e)}")
