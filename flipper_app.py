# flipper_app.py
# Main entry point - switches between windows/widgets

import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from views.MainMenu import MainMenu
from views.DeckBuilder import DeckBuilder
from views.QuizPlayer import QuizPlayer


class FlipperApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Initialize different screens/widgets
        self.main_menu = MainMenu(self)
        self.deck_builder = DeckBuilder(self)
        self.quiz_player = QuizPlayer(self)

        # Add to stacked widget and set index
        self.addWidget(self.main_menu)       # index 0
        self.addWidget(self.deck_builder)    # index 1
        self.addWidget(self.quiz_player)     # index 2

        self.setCurrentWidget(self.main_menu)

    def go_to_main_menu(self):
        self.setCurrentWidget(self.main_menu)

    def go_to_deck_builder(self):
        self.deck_builder.reset_ui()
        self.setCurrentWidget(self.deck_builder)

    def go_to_quiz_player(self, deck):
        self.quiz_player.load_deck(deck)
        self.setCurrentWidget(self.quiz_player)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    flipper = FlipperApp()
    flipper.setWindowTitle("Flipper")
    flipper.resize(600, 400)
    flipper.show()
    sys.exit(app.exec())
