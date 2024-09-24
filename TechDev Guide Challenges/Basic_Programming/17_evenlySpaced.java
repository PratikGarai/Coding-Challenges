import java.util.Scanner;

class EvenlySpaced
{
	public boolean evenlySpaced(int a, int b, int c) 
	{
  		if(a<=b && b<=c && b-a==c-b)
    			return true;
  		if(a<=c && c<=b && b-c==c-a)
    			return true;
  		if(b<=c && c<=a && b-c==c-a)
    			return true;
  		if(b<=a && a<=c && b-a==a-c)
    			return true;
  		if(c<=b && b<=a && c-b==b-a)
    			return true;
  		if(c<=a && a<=b && c-a==a-b)
    			return true;
  		return false;
	}

	public static void main(String[] args)
	{
		EvenlySpaced ob = new EvenlySpaced();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the 1st number : ");
		int a = in.nextInt();
		System.out.print("Enter the 2nd number : ");
		int b = in.nextInt();
		System.out.print("Enter the 3rd number : ");
		int c = in.nextInt();

		boolean d = ob.evenlySpaced(a,b,c);
		if(d)
			System.out.println("Evenly spaced");
		else
			System.out.println("Not evenly spaced");
	}
}
