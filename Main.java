/*
 *
 *
 *
 */


import java.util.Scanner;

public class Main {

	public static void main(String[] args){
	
		Scanner input = new Scanner(System.in);

		//constructs an array of empty card objects
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
				       shuffle();
					break;
				case ":c":
				       newCard(cardIndex);
				       cardIndex++;
				       break;
				case ":p":
					System.out.print("Enter card index: ");
				       int i = input.nextLine();
				       readCard(index);
				       break;
				case ":a":
				       printAll();
			}
		}
	}
	//creates new card
	public void newCard(index){
	
		String front;
		String back;

		System.out.print("\nEnter the front of the card: ");
		front = input.nextLine();
		System.out.print("\nEnter the back of the card: ");
		back = input.nextLine();
		cardArray[index] = new Card(front, back, index);
	}
	//removes a card
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
	//prints all cards
}
