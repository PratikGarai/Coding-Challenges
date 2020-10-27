import java.util.Scanner;

class MakeBricks
{
	public boolean makeBricks(int small, int big, int goal) 
	{
  		if((small+big*5)<goal)
    			return false;
  		if((goal/5)<=big)
    			if((goal%5)<=small)
      				return true;
    			else
      				return false;
  		else
    			if((goal-big*5)<=small)
      				return true;
    			else
      				return false;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		MakeBricks ob = new MakeBricks();
		System.out.print("Enter the number of small bricks : ");
		int a = in.nextInt();
		System.out.print("Enter the number of big bricks : ");
		int b = in.nextInt();
		System.out.print("Enter the goal : ");
		int c = in.nextInt();

		boolean res = ob.makeBricks(a,b,c);
		if(res)
			System.out.println("Possible");
		else
			System.out.println("Not possible");
	}
}
