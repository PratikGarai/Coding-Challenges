import java.util.Scanner;
import java.util.Arrays;

public class ArrayRearrangement
{

	Scanner in = new Scanner(System.in);
	String process()
	{
		int n = in.nextInt();
		int x = in.nextInt();
		
		int[] a = new int[n];
		int[] b = new int[n];
		for(int i=0;i<n;i++)
			a[i] = in.nextInt();
		for(int i=0;i<n;i++)
			b[i] = in.nextInt();

		Arrays.sort(a);
		Arrays.sort(b);
		for(int i=0;i<n;i++)
			if(a[i]+b[n-i-1]>x)
				return "No";

		return "Yes";
	}

	public static void main(String[] args)
	{
		ArrayRearrangement ob = new ArrayRearrangement();
		int n = ob.in.nextInt();
		for(int i=0;i<n;i++)
		{
			System.out.println(ob.process());
			ob.in.nextLine();
		}
	}
}
