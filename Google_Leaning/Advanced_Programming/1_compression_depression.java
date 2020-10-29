import java.util.Scanner;

class Compression_Depression 
{
	String a;
	Compression_Depression(String a)
	{
		this.a = a;
	}

	String decompress(int f, int l)
	{
		if(l-f<1)
			return "";
		if(!Character.isDigit(a.charAt(f)))
			return a.substring(f,l);
		String s = "";
		int ind = f;
		while(ind != l)
		{
			int n = 0, fb, lb;
			while(a.charAt(ind)!='[' && ind!=l)
			{
				n = n*10 + (a.charAt(ind)-'0');
				ind++;
			}
			fb = ind+1;
			while(a.charAt(ind)!=']' && ind!=l)
				ind++;
			lb = ind;
			ind++;
			String sub = decompress(fb,lb);
			for(int i=0;i<n;i++)
				s += sub;
		}
		return s;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the string : ");
		String a = in.next();
		Compression_Depression ob = new Compression_Depression(a);

		System.out.println("\nThe decompressed string is : "+ob.decompress(0,a.length()));
	}
}
