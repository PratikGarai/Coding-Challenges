import java.util.Scanner;

class BlackJack
{
	public int blackjack(int a, int b) 
	{
  		if(a>21 && b>21)
    			return 0;
  		if(a>21)
    			return b;
  		if(b>21)
    			return a;
  		return (a<b)?b:a;
	}

	public static void main(String[] args)
	{
		BlackJack ob = new BlackJack();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the 1st number : ");
		int a = in.nextInt();
		System.out.print("Enter the 2nd number : ");
		int b = in.nextInt();

		int c = ob.blackjack(a,b);
		System.out.println("Result : "+c);
	}
}
