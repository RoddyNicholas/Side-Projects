package sandbox;

import java.util.Scanner;

public class RelationshipSaver2
{
	public static void Menu() {
		System.out.println("\t--------------------------------------------------------------------------");
		System.out.println("\t\tWelcome to the best decision that you have made all day!\n");
		System.out.println("\t\t\t\tTHE RESTURAUNT FINDER v1.0\n");
		System.out.println("\t--------------------------------------------------------------------------");
	}
	
	public static void main(String[] args)
	{
		ResturauntPicker2 rp = new ResturauntPicker2();
		Scanner input = new Scanner(System.in);
		
		while(true) {
		Menu();
		System.out.print("\tWould you like me to help you find your next meal? (Y/N): ");
		
		String answer = input.nextLine();
		

		switch(answer) {
		case "Y":
		case "y":
			System.out.print("\n");
			rp.doWork();
			break;
		case "N":
		case "n":
			System.out.println("\n\tGood Bye!");
			break;
		default:
			System.out.println("\tPlease choose a valid option.\n");
			continue;
			}
		break;
		}
	}
}
