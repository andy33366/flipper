from Card import Card

def main():
    cardArray = []

    card0 = Card()

    print(card0.getQuestion())
    print(card0.getChoices())
    print(card0.checkAnswer("True"))


main()
