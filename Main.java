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
		//each card is constructed in arrayConstructor
		Card[] cardArray = new Card[10];//max number of cards is 10
		arrayConstructor(cardArray);
						
		String userInput = " ";
		int cardIndex = 0;
		int points = 0;

		System.out.println("Welcome to Flipper!\n");


		//menu loop
		while (!userInput.equals(":q")){

			//prints menu and grabs user input
			System.out.println("Enter :q to exit the program\nEnter :c to create a card\nEnter :s to shuffle cards\nEnter :p to look at a single card based on index\nEnter :a to print all cards\n");
			userInput = input.nextLine();

			switch (userInput){
			
				case ":q":
				       return;
				case ":s":
				       shuffle(cardArray, input, points);
					break;
				case ":c":
				       cardArray[cardIndex] = newCard(cardIndex, input);
				       cardIndex++;
				       System.out.println("The maximum amount of cards is 10. you are currently at "+cardIndex);
				       break;
				case ":p":
					System.out.print("Enter card index: ");
				       int i = input.nextInt();
				       input.nextLine();
				       readCard(i, cardArray, input);
				       break;
				case ":a":
				       printAll(cardArray);
					break;
				default :
				       System.out.println("Invalid command");
				       break;

			}
		}
	}
	//constructs the array of cards
	public static Card[] arrayConstructor(Card[] cardArray){
	
		//for length of cardArray
		//for(int i = 0; i < cardArray.length; i++){
		
			//PROBLEM: how do I create variables programmatically?
		//}

		String blank = " ";
		Card card0 = new Card(blank, blank, 0);
		cardArray[0] = card0;
		Card card1 = new Card(blank, blank, 1);
		cardArray[1] = card1;
		Card card2 = new Card(blank, blank, 2);
		cardArray[2] = card2;
		Card card3 = new Card(blank, blank, 3);
		cardArray[3] = card3;
		Card card4 = new Card(blank, blank, 4);
		cardArray[4] = card4;
		Card card5 = new Card(blank, blank, 5);
		cardArray[5] = card5;
		Card card6 = new Card(blank, blank, 6);
		cardArray[6] = card6;
		Card card7 = new Card(blank, blank, 7);
		cardArray[7] = card7;
		Card card8 = new Card(blank, blank, 8);
		cardArray[8] = card8;
		Card card9 = new Card(blank, blank, 9);
		cardArray[9] = card9;

		
		return cardArray;

	}
	//creates new card
	public static Card newCard(int index, Scanner input){
	
		String front;
		String back;

		System.out.print("\nEnter the front of the card: ");
		front = input.nextLine();
		System.out.print("\nEnter the back of the card: ");
		back = input.nextLine();
		Card card = new Card(front, back, index);
		return card;

	}
	//removes a card
	public static void removeCard(int index, Card[] cardArray){
	
		cardArray[index] = new Card();//replaces cardArray[index] with an empty card object
	}
	//reads a card
	public static void readCard(int index, Card[] cardArray, Scanner input){
	
		System.out.println(cardArray[index].getFront());//prints out front of card
		String userAnswer = input.nextLine();

		cardArray[index].flip(userAnswer);
	}
	//shuffles cards
	public static void shuffle(Card[] cardArray, Scanner input, int points){
	
		String userInput = " ";
		int[] shuffleArray = new int[10];
		
		System.out.println("\nEnter :q to exit shuffle mode\nEnter :n to skip to next card\nEnter :b for previous card\nEnter :p to print your current points\n");

		//big loop
		while (!userInput.equals(":q")){ 
			
			System.out.println("You currently have "+points+" points! Press enter to continue or :q to exit shuffle mode.");
			userInput = input.nextLine();
			if (userInput.equals(":q")){
				return;
			}

			//creates a randomized array of of currently used indexes 
			for( int i = 0; i < cardArray.length; i++){
				//random number between 0-9
				int randNum = (int)(Math.random()*10);
				//assigns the random number to shufflearray index
				shuffleArray[i] = randNum;
			}
			//loops through the random array
			for (int j = 0; j < shuffleArray.length; j++){ 
				
				System.out.println("\nCard #"+shuffleArray[j]+"\n");
				System.out.println(cardArray[shuffleArray[j]].getFront());
				System.out.println("\n===============================================================\n");
				userInput = input.nextLine();
			
				switch (userInput){
			
					case ":q":
					       return;
					case ":n":
					       //next card
	
						break;
					case ":b":
					       //previous card
					       j--;
					       j--;
					       break;
					case ":p":
					       //print current points
					       System.out.println("\nYou currently have "+points+" points!");
					  
					default :
					       //flip card
					       if(cardArray[j].flip(userInput)){
						       points++;
					       }
					       break;
				}
			

			}	
			if (userInput.equals(":q")){
				return;
			}

		//once loop ends goes back to big loop and creates a new random array
		//
		}
	}
	//prints all cards
	public static void printAll(Card[] cardArray){
	
		//for i in cardArray printCard()
		for( int i = 0; i < cardArray.length; i++){
			System.out.println("\nCard #"+i+"\n");
			System.out.println(cardArray[i].getFront());
			System.out.println(cardArray[i].getBack());
			System.out.println("\n===============================================================\n");
		}

	}
}
