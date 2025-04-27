#Card.py
#controlls card and deck classes

#to turn cards to from json and save to computer
import json
import os

class Card:
    def __init__(self, question, choices, answer_index ):
        #the text of the flashcard
        self.question = question
        #list of answer options
        self.choices = choices
        #answer will be an index in the choices array
        #eg. answer ==> self.choices[i]
        self.answer_index = answer_index


    def check_answer(self, selected_index):
        return self.answer_index == selected_index

    #converts Card into a dictionary for storage
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer_index": self.answer_index
        }

    #converts dictionary to card
    @staticmethod
    def from_dict(data):
        return Card(data["question"], data["choices"], data["answer_index"])

class Deck:
    def __init__(self, name="Untitled Deck"):
        self.name = name
        #stores Card objects
        self.cards = []

    #adds card to deck
    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, index):
        return self.cards[index] if 0 <= index < len(self.cards) else None
        '''
        if 0 <= index < len(self.cards):
            return self.cards[index]
        else:
            return None
        '''

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    #saves deck to computer
    def save_to_file(self, directory="decks"):
        #if /decks doesnt exist on the machine make one
        if not os.path.exists(directory):
            os.makedirs(directory)
        #filepath is decks/<deckname>.json
        path = os.path.join(directory, f"{self.name}.json")
        data = {
            "name": self.name,
            "cards": [card.to_dict() for card in self.cards]
        }
        #opens file dumps data into file
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    #rebuilds the deck from stored json
    @staticmethod
    def load_from_file(filename, directory="decks"):
        path = os.path.join(directory, filename)
        #grabs data from file
        with open(path, "r") as f:
            data = json.load(f)
        deck = Deck(data["name"])
        #grabs each card from data
        for card_data in data["cards"]:
            deck.add_card(Card.from_dict(card_data))
        return deck
'''
    def getQuestion(self):
        return self.question

    def getChoices(self):
        return self.choices

    def getAnswer(self):
        return self.answer

    def setQuestion(self, question):
        self.question = question

    def setChoices(self, choices):
        self.choices = choices

    def checkAnswer(self, answer):
        return self.choices[self.answer] == self.choices[answer]

'''
        
