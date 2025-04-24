# views/QuizPlayer.py
# Allows users to go through a flashcard quiz

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from models.Card import Deck

class QuizPlayer(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.deck = None
        self.current_index = 0
        self.score = 0

        self.layout = QVBoxLayout()
        self.question_label = QLabel("Question will appear here")
        self.layout.addWidget(self.question_label)

        self.answer_buttons = []
        # Adds answer choices to UI
        for i in range(5):  # max 5 choices per card
            btn = QPushButton()
            btn.clicked.connect(self.make_answer_handler(i))
            btn.hide()  # only show needed ones later
            self.answer_buttons.append(btn)
            self.layout.addWidget(btn)

        self.setLayout(self.layout)

    def load_deck(self, deck):
        self.deck = deck
        self.current_index = 0
        self.score = 0
        self.show_card()

    def show_card(self):
        # Ends quiz if index is out of bounds
        if self.current_index >= len(self.deck):
            self.finish_quiz()
            return

        card = self.deck.get_card(self.current_index)
        self.question_label.setText(card.question)

        # Show the appropriate number of answer buttons
        for i, btn in enumerate(self.answer_buttons):
            if i < len(card.choices):
                btn.setText(card.choices[i])
                btn.show()
            else:
                btn.hide()

    def make_answer_handler(self, index):
        def handler():
            card = self.deck.get_card(self.current_index)
            if card.check_answer(index):
                self.score += 1
                QMessageBox.information(self, "Correct!", "Nice job!")
            else:
                correct_text = card.choices[card.answer_index]
                QMessageBox.information(self, "Incorrect!", f"The correct answer is: {correct_text}")

            self.current_index += 1
            self.show_card()
        return handler

    def finish_quiz(self):
        QMessageBox.information(self, "Quiz Complete", f"You got {self.score} out of {len(self.deck)} correct!")
        self.app.go_to_main_menu()
