package sandbox;

import java.util.Random;

class ResturauntPicker2 {
	 
	public ResturauntPicker2()
	{
		
	}
	public void doWork() {
	   
	    Random restaurant = new Random();

	    //Picks
	    int num = restaurant.nextInt(15)+1;

	    //Sorts
	    switch(num)
	    {
	      case 1:
	      System.out.println("\tYou are eating Pizza Hut.");
	      break;
	      case 2:
	      System.out.println("\tYou are eating Taco Bell.");
	      break;
	      case 3:
	      System.out.println("\tYou are eating Chick-Fil-A.");
	      break;
	      case 4: 
	      System.out.println("\tYou are eating Wendy's.");
	      break;
	      case 5:
	      System.out.println("\tYou are eating Hardee's.");
	      break;
	      case 6:
	      System.out.println("\tYou are eating McDonald's.");
	      break;
	      case 7:
	      System.out.println("\tYou are eating Popeye's.");
	      break;
	      case 8:
	      System.out.println("\tYou are eating Arby's.");
	      break;
	      case 9:
	      System.out.println("\tYou are eating Culver's.");
	      break;
	      case 10:
	      System.out.println("\tYou are eating Panera Bread.");
	      break;
	      case 11:
	      System.out.println("\tYou are eating Panda Express.");
	      break;
	      case 12:
	      System.out.println("\tYou are eating Mugsy's.");
	      break;
	      case 13:
	      System.out.println("\tYou are eating Jimmy Johns.");
	      break;
	      case 14:
	      System.out.println("\tYou are eating Great Wall.");
	      break;
	      case 15:
	      System.out.println("\tYou are eating Braize Subs.");
	    }
	  }
	}
