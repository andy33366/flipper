#Card.py
#controlls card and deck classes

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
        
