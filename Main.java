/*
 *
 *
 *
 */


import java.util.Scanner;

public class Main {

	public static void main(String[] args){
	
		Scanner input = new Scanner(System.in);

		//creates an array of empty card objects
		//each card is constructed in newCard()
		Card[] cardArray = new Card[30]//max number of cards is 30
						
		String userInput = " ";
		int cardIndex = 0;
		int points = 0;

		System.out.println("Welcome to Flipper!\n");

		//menu loop
		while (!userInput.equals(":q")){

			//prints menu and grabs user input
			System.out.println("Enter :q to exit the program\nEnter :c to create a card\nEnter :s to shuffle cards\nEnter :p to look at a single card based on index\nEnter :a to print all cards\nEnter :r to remove a card");
			userInput = input.nextLine();

			switch (userInput){
			
				case ":q":
				       return;
				       break;
				case ":s":
				       shuffle(cardArray);
					break;
				case ":c":
				       newCard(cardIndex);
				       cardIndex++;
				       break;
				case ":p":
					System.out.print("Enter card index: ");
				       int i = input.nextLine();
				       readCard(cardIndex);
				       break;
				case ":a":
				       printAll(cardArray);
			}
		}
	}
	//creates new card
	public void newCard(int index){
	
		String front;
		String back;

		System.out.print("\nEnter the front of the card: ");
		front = input.nextLine();
		System.out.print("\nEnter the back of the card: ");
		back = input.nextLine();
		cardArray[index] = new Card(front, back, index);
	}
	//removes a card
	public void removeCard(int index){
	
		cardArray[index] = new Card();//replaces cardArray[index] with an empty card object
	}
	//reads a card
	public void readCard(index){
	
		String userAnswer;

		System.out.println(cardArray[index].front);//prints out front of card
		userAnswer = input.nextLine();

		if (cardArray[index].flip(userAnswer)){
		
			points++;
		}
	}
	//shuffles cards
	public void shuffle(){
	
		//big loop 
		//prints menu :q to exit shuffle mode :n for next card, :b for previous card, :p to print points
		//creates a randomized array of of currently used indexes 
		//
		//loops through the random array
		//once loop ends goes back to big loop and creates a new random array
		//
	}
	//prints all cards
	public void printAll(){
	
		//for i in cardArray printCard()
	}
}
