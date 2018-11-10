import java.util.Scanner;
//https://open.kattis.com/problems/hangingout
//Hanging Out on the Terrace

public class HangingOutontheTerrace {

	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int safe=x.nextInt();
		int N = x.nextInt();
		int peopleOnDeck=0;
		int groups=0;
		int declinedGroups=0;
		for(int i=0;i<N;i++) {
			String type=x.next();
			int amount=x.nextInt();
			if(type.equals("enter")) {
				if(peopleOnDeck+amount<=safe) {
					peopleOnDeck+=amount;
					if(amount>1) {
						groups++;
						}
				}else {
					declinedGroups++;
					
				}
				}
			
			if(type.equals("leave")) {
				peopleOnDeck-=amount;
			}
			
			
			
		}
		
		System.out.println(declinedGroups);
	}

}
