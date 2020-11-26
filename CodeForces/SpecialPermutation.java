import java.util.Scanner;

public class SpecialPermutation
{
	void printStuff(int n)
	{
		System.out.print(n+" ");
		for(int i=1;i<=n-1;i++)
			System.out.print(i+" ");
		System.out.println();
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		SpecialPermutation ob = new SpecialPermutation();
		int n = in.nextInt();
		for(int i=0;i<n;i++)
			ob.printStuff(in.nextInt());
	}
}
