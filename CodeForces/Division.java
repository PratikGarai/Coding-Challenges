import java.util.Scanner;

public class Division
{
	Scanner in = new Scanner(System.in);

	int process()
	{
		int p = in.nextInt();
		int q = in.nextInt();

		if (q>p)
			return q;

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
