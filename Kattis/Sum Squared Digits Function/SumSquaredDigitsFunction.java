import java.util.Scanner;

public class SumSquaredDigitsFunction {

	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		int N = x.nextInt();
		
		while(N>0) {
			int k, b, n;
			k=x.nextInt();
			b=x.nextInt();
			n=x.nextInt();
//			System.out.printf("\n%d %d %d\n",k,b,n);
			int ssd=0;
			
			while(n>0) {
				ssd += (n % b) * (n % b);
			    n /= b;
				
			}
			System.out.printf("%d %d\n",k,ssd);
			N--;
		}
	}

}
