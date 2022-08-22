package connector;

import java.util.Scanner;

import states.HasQuarter;
import states.NoQuarter;
import states.OutOfGumballs;
import states.State;

class GumBallMachineContext {
	
	private int numberOfGums = 0;
	private State state = HasQuarter.Instance();
	
	public static void main(String[] args) {
		
		System.out.println("beep");
		
	}
	
	public void work() {
		System.out.println("Insert number of gums (0 for EXIT): ");
		Scanner s = new Scanner(System.in);
		int choice;
		try {
			choice = s.nextInt();
		}
		catch (Exception e) {
			return;
		}
		if (choice == 0) {
			System.out.println("Bye bye");
			return;
		}
		
	}

	public boolean ejectQuarter(int amount) {
		while (amount > 0) {
			amount--;
			numberOfGums--;
			if (numberOfGums == 0) {
				state = NoQuarter.Instance();
				return false;
			}
		}
		
		return true;
	}
	
}