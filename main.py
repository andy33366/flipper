from Card import Card

def main():
    cardArray = deckMaker()
    for i in cardArray:
        print(i.getQuestion())
        print(i.getChoices())
        print(i.getAnswer())


    #while stop != true : show card + check answer
    while choice != "!q":
        #for each card in cardArray show q and check provided answer
        for i in cardArray:
            print(i.getQuestion())
            menu = ""
            for c in i.getChoices:
                menu = menu + str(c) + " " + str(choices.index(c)) + "\n"
            print(menu)
            answer = int(input())
            if i.checkAnswer(answer):
                print("correct!")
            else:
                print("wrong!")
            




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


main()
