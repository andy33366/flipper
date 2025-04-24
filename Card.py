
class Card:
    def __init__(self, question = "Empty", choices = ["True", "False"], answer = 0 ):
        self.question = question
        self.choices = choices
        #answer will be an index in the choices array
        #eg. answer ==> self.choices[i]
        self.answer = answer

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
        
