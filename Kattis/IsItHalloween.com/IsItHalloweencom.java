import java.util.Scanner;
//https://open.kattis.com/problems/isithalloween
//IsItHalloween.com

public class IsItHalloweencom {
	
	
	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		String date=x.nextLine();
//		int date=x.nextInt();

		if(date.equals("OCT 31")||date.equals("DEC 25")) {
			System.out.print("yup");
		}else {
			System.out.println("nope");
		}
		
	}

}
