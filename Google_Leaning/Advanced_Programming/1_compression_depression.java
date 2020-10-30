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
		if(f>l)
			return "";
		if(Character.isDigit(a.charAt(f)))
		{
			String s = "";
			int ind = f;
			int n=0;
			while(Character.isDigit(a.charAt(ind)))
			{
				n = n*10 + a.charAt(ind) -'0';
				ind++;
			}
			ind++;
			int bractes = 1, begin = ind;
			while(bractes!=0)
			{
				if(a.charAt(ind)=='[')
					bractes++;
				if(a.charAt(ind)==']')
					bractes--;
				ind++;
			}
			int end = ind-2;
			System.out.println(begin+" "+end);
			String st = decompress(begin, end);
			System.out.println(st);
			for(int i=0;i<n;i++)
				s += st;
			return s;
		}
		else
		{
			return a.substring(f,l+1);
		}

	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the string : ");
		String a = in.next();
		Compression_Depression ob = new Compression_Depression(a);

		System.out.println("\nThe decompressed string is : "+ob.decompress(0,a.length()-1));
	}
}
