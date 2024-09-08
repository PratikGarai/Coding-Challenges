import java.util.Scanner;

public class Division
{
	Scanner in = new Scanner(System.in);

	long process()
	{
		long p = in.nextLong();
		long q = in.nextLong();

		if (q>p)
			return p;
		
		if(p%q!=0)
			return p;

		long max = 1;
		for(long i=1;i<=(long)(Math.ceil(Math.pow(p,0.5)));i++)
		{
			if(p%i==0 && i%q!=0)
				max = i;
		}

		return max;

	}

	public static void main(String[] args)
	{
		Division ob = new Division();
		int n = ob.in.nextInt();
		for(int i=0;i<n;i++)
		{
			System.out.println(ob.process());
		}
	}
}
