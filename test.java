import java.util.Scanner;

public class test {

	public static void main(String[] args){
	
		Scanner input = new Scanner(System.in);

		String front;
		front = input.nextLine();
		String back;
		back = input.nextLine();

		Card card0 = new Card();
		Card card1 = new Card(front, back, 1);

		System.out.println("card0");
		System.out.println(card0.getFront());
		System.out.println(card0.getBack());
		System.out.println("card1");

		System.out.println(card1.getFront());
		System.out.println(card1.getBack());
		System.out.println();
		Card[] cards = {card0, card1};
		System.out.println("cards[0]");

		System.out.println(cards[0].getFront());
		System.out.println("cards[1]");

		System.out.println(cards[1].getFront());

		String i;
		i = input.nextLine();
		System.out.println(card0.flip(i));

		System.out.println(card1.getFront());
		System.out.println(card1.getBack());

		i = input.nextLine();
		System.out.println(card1.flip(i));


	}
}
