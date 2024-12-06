/*
 *
 *
 *
 */

public class Card{

	//data fields
	
	//front of card
	String front = " ";
	//back of card
	String back = " ";
	int index;

	//MAKE CARD ARRAY IN MAIN NOT HERE
	//card array
	//static this[] cardArray = new this[50];//max number of cards is 50
	//current index cardArray is at
	//static int currentIndex = 0;


	//methods
	
	//constructor
	public Card(){
	
		front = " ";//default is empty string
		back = " ";
		index = 0;

		//assigns the card index
		//currentIndex ++;
		//adds card object to the card array at the current index
		//cardArray[currentIndex] = this;

	}
	public Card(String cardFront, String cardBack, int i){
	
		front = cardFront;
		back = cardBack;
		index = i;

		//assigns card index
		//currentIndex ++;
		//adds card object to the card array at the current index
		//cardArray[currentIndex] = this;

	}
	//flip card(check answer)
	public Boolean flip(String userAnswer){
	

		//if userAnswer == back --> correct so +1 point
		if (userAnswer.equals(this.back)){
			System.out.println("Correct! +1 point");

			return true;
		}
		else{
		
			System.out.println("Wrong! The correct answer should be:\n");
			System.out.println(this.back); //prints back of the card
			return false;
		}
	}
	//getFront
	public String getFront(){
	
		System.out.println(this.front);
		return this.front;
	}
	//
}
