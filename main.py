'''
gonna copy kahoot quiz builder UI:

    type question

    add answer choices (start with two, button to add more)
    each answer choice has checkable button for correct answer

    button to save card

    button to add new card

    DONEEEEEE

'''

# imports custom card class
from Card import Card
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QCheckBox, QHBoxLayout, QGridLayout
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Initializing MainWindow")
        self.setWindowTitle("Flipper")
        self.setMinimumSize(QSize(400, 300))

        self.layout = QVBoxLayout()

        #adds a line to the layout to enter a question
        self.questionInput = QLineEdit(self)
        self.questionInput.setPlaceholderText("Enter question")
        self.layout.addWidget(self.questionInput)

        #array for the answer choices and which is correct
        self.choiceInputs = []
        self.choiceCheckboxes = []

        #puts the choices in a grid
        self.choiceLayout = QGridLayout()
        self.layout.addLayout(self.choiceLayout)

        #adds 2 choice inputs
        for i in range(2):
            self.addChoiceInput(i)

        #when clicked, adds now choice input
        self.addChoiceButton = QPushButton("Add New Answer Choice", self)
        self.addChoiceButton.clicked.connect(self.addChoiceInput)
        self.layout.addWidget(self.addChoiceButton)

        #when clicked adds the card to deck
        self.addCardButton = QPushButton("Add Card", self)
        self.addCardButton.clicked.connect(self.addCard)
        self.layout.addWidget(self.addCardButton)

        #allows user to edit previous cards
        self.previousCardButton = QPushButton("Previous Card", self)
        self.previousCardButton.clicked.connect(self.previousCard)
        self.layout.addWidget(self.previousCardButton)

        #when user is finished building deck
        self.doneButton = QPushButton("Done Building My Deck", self)
        self.doneButton.clicked.connect(self.finishDeckBuilding)
        self.layout.addWidget(self.doneButton)

        #main widget
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)

        #initializes card array
        self.cards = []
        self.currentCardIndex = 0
        print("MainWindow initialized")

    def addChoiceInput(self, index=None):
        #adds a new choice input field and checkbox to the layout ony 2 - 5 choices allowed
        try:
            print("Adding choice input")
            if len(self.choiceInputs) < 5:
                #create answer choice box and checkbox to say if it is correct
                choiceInput = QLineEdit(self)
                choiceInput.setPlaceholderText(f"Enter choice {len(self.choiceInputs) + 1}")
                choiceCheckbox = QCheckBox("Correct", self)

                #makes answer choices layout be in 2 columns
                row = len(self.choiceInputs) // 2
                col = len(self.choiceInputs) % 2

                self.choiceLayout.addWidget(choiceInput, row, col * 2)
                self.choiceLayout.addWidget(choiceCheckbox, row, col * 2 + 1)

                self.choiceInputs.append(choiceInput)
                self.choiceCheckboxes.append(choiceCheckbox)
            else:
                print("Maximum of 5 answer choices reached.")
        except Exception as e:
            print(f"Error adding choice input: {e}")

    def addCard(self):
        #adds the card to the deck based on user input
        try:
            print("Adding card")
            question = self.questionInput.text()
            #for every choice input the user added to the card, it adds the text to the choices list
            choices = [choiceInput.text() for choiceInput in self.choiceInputs]
            
            #checks if no checkboxes are checked/ adds indexes of checked box to answer
            #[i for i, checkbox in enumerate(self.choiceCheckboxes) if checkbox.isChecked()]
            answer = next((i for i, checkbox in enumerate(self.choiceCheckboxes) if checkbox.isChecked()), None)

            if answer is not None:
                card = Card(question, choices, answer)
                if self.currentCardIndex < len(self.cards):
                    self.cards[self.currentCardIndex] = card
                else:
                    self.cards.append(card)
                self.resetInputs()
                self.currentCardIndex = len(self.cards)
                print(f"Added card: {question}, {choices}, {answer}")
            else:
                print("Please select the correct answer.")
        except IndexError as e:
            print(f"IndexError: {e}")
            print(str(len(self.cards)))
            print(str(self.currentCardIndex))
            self.cards.append(card)
            self.resetInputs()
            self.currentCardIndex = len(self.cards)
        except Exception as e:
            print(f"Error adding card: {e}")

    def resetInputs(self):
        #Resets the input fields for a new card
        try:
            print("Resetting inputs")
            self.questionInput.clear()
            for choiceInput in self.choiceInputs:
                choiceInput.deleteLater()
            for choiceCheckbox in self.choiceCheckboxes:
                choiceCheckbox.deleteLater()
            self.choiceInputs = []
            self.choiceCheckboxes = []
            for i in range(2):
                self.addChoiceInput(i)
        except Exception as e:
            print(f"Error resetting inputs: {e}")

    def previousCard(self):
        #Loads the previous card for editing
        try:
            print("Loading previous card")
            if self.currentCardIndex > 0:
                self.currentCardIndex -= 1
                card = self.cards[self.currentCardIndex]
                self.questionInput.setText(card.getQuestion())
                self.resetInputs()
                for i, choice in enumerate(card.getChoices()):
                    self.addChoiceInput(i)
                    self.choiceInputs[i].setText(choice)
                    self.choiceCheckboxes[i].setChecked(i == card.getAnswer())
        except Exception as e:
            print(f"Error loading previous card: {e}")

    def finishDeckBuilding(self):
        """Finishes deck building and prompts the user to name the deck."""
        try:
            print("Finishing deck building")
            self.clearLayout(self.layout)

            self.deckNameInput = QLineEdit(self)
            self.deckNameInput.setPlaceholderText("Enter deck name")
            self.layout.addWidget(self.deckNameInput)

            self.finishButton = QPushButton("Finish", self)
            self.finishButton.clicked.connect(self.saveDeck)
            self.layout.addWidget(self.finishButton)

            self.backButton = QPushButton("Back", self)
            self.backButton.clicked.connect(self.backToDeckBuilder)
            self.layout.addWidget(self.backButton)

            self.centralWidget.setLayout(self.layout)
        except Exception as e:
            print(f"Error finishing deck building: {e}")

    def clearLayout(self, layout):
        """Clears the existing layout."""
        try:
            print("Clearing layout")
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        except Exception as e:
            print(f"Error clearing layout: {e}")

    def saveDeck(self):
        """Saves the deck and returns to the main menu."""
        try:
            print("Saving deck")
            deckName = self.deckNameInput.text()
            print(f"Deck '{deckName}' created with {len(self.cards)} cards.")
            # Here you can implement saving the deck to a file or database
            self.showMainMenu()
        except Exception as e:
            print(f"Error saving deck: {e}")

    def backToDeckBuilder(self):
        """Returns to the deck builder."""
        try:
            print("Returning to deck builder")
            self.clearLayout(self.layout)
            self.layout.addWidget(self.questionInput)
            self.layout.addLayout(self.choiceLayout)
            self.layout.addWidget(self.addChoiceButton)
            self.layout.addWidget(self.addCardButton)
            self.layout.addWidget(self.previousCardButton)
            self.layout.addWidget(self.doneButton)
            self.centralWidget.setLayout(self.layout)
        except Exception as e:
            print(f"Error returning to deck builder: {e}")

    def showMainMenu(self):
        """Displays the main menu for selecting a deck to study."""
        try:
            print("Showing main menu")
            self.clearLayout(self.layout)

            self.deckSelectionLabel = QLabel("Select a deck to study:", self)
            self.layout.addWidget(self.deckSelectionLabel)

            # Here you can implement loading available decks and displaying them as buttons
            # For simplicity, let's assume we have a list of deck names
            deckNames = ["Deck 1", "Deck 2", "Deck 3"]
            for deckName in deckNames:
                deckButton = QPushButton(deckName, self)
                deckButton.clicked.connect(lambda checked, name=deckName: self.startQuiz(name))
                self.layout.addWidget(deckButton)

            self.centralWidget.setLayout(self.layout)
        except Exception as e:
            print(f"Error showing main menu: {e}")

    def startQuiz(self, deckName):
        """Starts the quiz for the selected deck."""
        try:
            print("Starting quiz")
            self.clearLayout(self.layout)

            self.questionLabel = QLabel("Question will be displayed here", self)
            self.layout.addWidget(self.questionLabel)

            self.answerButtons = []
            for i in range(5):  # Assuming a maximum of 5 answer choices
                answerButton = QPushButton(f"Choice {i+1}", self)
                answerButton.clicked.connect(lambda checked, index=i: self.checkAnswer(index))
                self.layout.addWidget(answerButton)
                self.answerButtons.append(answerButton)

            self.centralWidget.setLayout(self.layout)
            self.currentCardIndex = 0
            self.score = 0
            self.loadCard(deckName)
        except Exception as e:
            print(f"Error starting quiz: {e}")

    def loadCard(self, deckName):
        """Loads the next card in the deck."""
        try:
            print("Loading card")
            # Here you can implement loading the deck from a file or database
            # For simplicity, let's assume we have a list of cards
            self.cards = [Card("Sample Question", ["Choice 1", "Choice 2", "Choice 3", "Choice 4", "Choice 5"], 2)]
            if self.currentCardIndex < len(self.cards):
                card = self.cards[self.currentCardIndex]
                self.questionLabel
        except:
            print("Failed to load card")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()








'''
        #Button to create new card
        button = QPushButton("Add new card")
        button.setCheckable(True)
        button.clicked.connect(self.buttonClicked)

        #button to set answer choice as correct
        self.buttonChecked = False
        correctButton = QPushButton("correct")
        correctButton.setCheckable(True)
        correctButton.setChecked(self.buttonChecked)
        correctButton.clicked.connect(self.correctButton)

        #decides size, etc of main window
        self.setMinimumSize(QSize(400, 300))
        self.setCentralWidget(correctButton)

    def buttonClicked(self):
        print("clicked")
        #

    def correctButton(self, checked):
        self.buttonChecked = checked
        print(self.buttonChecked)

    def main():
        cardArray = deckMaker()
        for i in cardArray:
            print(i.getQuestion())
            print(i.getChoices())
            print(i.getAnswer())


        #while stop != true : show card + check answer
        choice = ""
        while choice != "!q":
            #for each card in cardArray show q and check provided answer
            for i in cardArray:
                print(i.getQuestion())
                menu = ""
                choices = i.getChoices()
                for c in choices:
                    menu = menu + str(c) + " " + str(choices.index(c)) + "\n"
                print(menu)
                answer = int(input())
                if i.checkAnswer(answer):
                    print("correct!")
                else:
                    print("wrong!")
                    print(f"correct answer is {i.getAnswer()}")
                

TODO: split into client-side code and server-side code


def deckMaker():
    #makes the card deck
    cardArray = []
    
    #while stop != true : add cards to array
    config = True
    while config:

        #ask for Q
        question = input("Question: ")

        #ask for choices (enter !q to finish)
        choices = []
        choice = ""
        while choice != "!q":
            choice = input("Answer choice: ")
            if choice == "!q":
                break
            choices.append(choice)
        
        #ask for correct answer
        print("Which of these is the correct answer?")
        menu = ""
        for i in choices:
            menu = menu + str(i) + " " + str(choices.index(i)) + "\n"
        print(menu)
        answer = int(input())

        #make card object and add to card Array
        cardArray.append(Card(question, choices, answer))
        if input("Enter \"!q\" to stop adding cards") == "!q":
            config = False

    return cardArray

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
'''
