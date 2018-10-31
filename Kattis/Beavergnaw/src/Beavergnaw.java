import java.util.Scanner;

public class Beavergnaw {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int D=sc.nextInt();
		int V=sc.nextInt();
		while(D!=0 && V!=0) {
			
			
			
			double d3 = D*D*D - 6*V/Math.PI;
	        double d = Math.pow(d3, 1/3.0);
			
			System.out.println(d);
			
			D=sc.nextInt();
			V=sc.nextInt();
			
		}
	}

}
