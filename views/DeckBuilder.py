# views/DeckBuilder.py
# Allows users to create flashcards and build a deck

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLineEdit, QLabel, QCheckBox, QGridLayout, QMessageBox)
from models.Card import Card, Deck

class DeckBuilder(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.deck = Deck()
        self.current_card_index = None  # Track if editing an existing card

        self.layout = QVBoxLayout()

        # Input for the flashcard question
        self.question_input = QLineEdit()
        self.question_input.setPlaceholderText("Enter the question")
        self.layout.addWidget(self.question_input)

        # Grid for choices and checkboxes
        self.choices_layout = QGridLayout()
        self.choice_inputs = []
        self.correct_checkboxes = []
        self.layout.addLayout(self.choices_layout)

        for _ in range(2):
            self.add_choice()

        # Buttons
        add_choice_btn = QPushButton("Add Choice")
        add_choice_btn.clicked.connect(self.add_choice)
        self.layout.addWidget(add_choice_btn)

        add_card_btn = QPushButton("Add Card to Deck")
        add_card_btn.clicked.connect(self.add_card)
        self.layout.addWidget(add_card_btn)

        prev_card_btn = QPushButton("Previous Card")
        prev_card_btn.clicked.connect(self.load_previous_card)
        self.layout.addWidget(prev_card_btn)

        self.deck_name_input = QLineEdit()
        self.deck_name_input.setPlaceholderText("Name your deck")
        self.layout.addWidget(self.deck_name_input)

        finish_btn = QPushButton("Finish Deck")
        finish_btn.clicked.connect(self.finish_deck)
        self.layout.addWidget(finish_btn)

        back_btn = QPushButton("Back to Menu")
        back_btn.clicked.connect(self.app.go_to_main_menu)
        self.layout.addWidget(back_btn)

        self.setLayout(self.layout)

		#adds answer choices
    def add_choice(self):
        if len(self.choice_inputs) >= 5:
            QMessageBox.warning(self, "Limit Reached", "You can only add up to 5 choices.")
            return

				#creates 2 columns for a preety layout :)
        row = len(self.choice_inputs) // 2
        col = (len(self.choice_inputs) % 2) * 2

				#empty box for answer choice
        choice_input = QLineEdit()
        #setPlaceholderText says choice 1 or choice 2 etc
        choice_input.setPlaceholderText(f"Choice {len(self.choice_inputs) + 1}")
        checkbox = QCheckBox("Correct")

        self.choices_layout.addWidget(choice_input, row, col)
        self.choices_layout.addWidget(checkbox, row, col + 1)

        self.choice_inputs.append(choice_input)
        self.correct_checkboxes.append(checkbox)

    def add_card(self):
        question = self.question_input.text()
        #if the field is not empty, take text and add it to choices (for each choice)
        choices = [field.text() for field in self.choice_inputs if field.text().strip()]
        #if checkbox is checked, add index of checkbox to correct answer list
        correct_indexes = [i for i, cb in enumerate(self.correct_checkboxes) if cb.isChecked()]

        if not question or len(choices) < 2:
            QMessageBox.warning(self, "Invalid Card", "Please enter a question and at least 2 choices.")
            return
        if len(correct_indexes) != 1:
            QMessageBox.warning(self, "Invalid Answer", "Exactly one choice must be marked as correct.")
            return

        card = Card(question, choices, correct_indexes[0])

				#checks if this is a new card to add to the deck or an existing card being edited
        if self.current_card_index is not None:
            self.deck.cards[self.current_card_index] = card
        else:
            self.deck.add_card(card)

        self.clear_card_inputs()
        self.current_card_index = None

    def clear_card_inputs(self):
				#clears question field
        self.question_input.clear()
        #for all answer chouces removes inputs
        for i in range(len(self.choice_inputs)):
            self.choice_inputs[i].deleteLater()
            self.correct_checkboxes[i].deleteLater()
				#defaults to empty values and 2 answer choices
        self.choice_inputs = []
        self.correct_checkboxes = []
        for _ in range(2):
            self.add_choice()

    def load_previous_card(self):
        if len(self.deck.cards) == 0:
            QMessageBox.information(self, "No Cards", "There are no cards to edit yet.")
            return

				#if not editing a card go to last card in the deck
        if self.current_card_index is None:
            self.current_card_index = len(self.deck.cards) - 1
				#else go to previous card
        else:
            self.current_card_index = max(0, self.current_card_index - 1)

        card = self.deck.cards[self.current_card_index]

        self.question_input.setText(card.question)
        self.clear_card_inputs()

				#fills previous card values into UI
        for i, choice in enumerate(card.choices):
            self.add_choice()
            self.choice_inputs[i].setText(choice)
            self.correct_checkboxes[i].setChecked(i == card.answer_index)

    def finish_deck(self):
        name = self.deck_name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Missing Deck Name", "Please name your deck.")
            return
        self.deck.name = name
        # Normally save deck to file/db here
        QMessageBox.information(self, "Deck Saved", f"Deck '{name}' with {len(self.deck)} cards saved!")
        self.app.go_to_main_menu()

    def reset_ui(self):
        self.deck = Deck()
        self.deck_name_input.clear()
        self.clear_card_inputs()
        self.current_card_index = None
