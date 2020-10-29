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
		if(l-f==1)
			return String.valueOf(a.charAt(f));
		String s="", sub="";
		int ind = f, n=0,fb=f;
		boolean tracking = false;
		while(ind!=l)
		{
			if(Character.isDigit(a.charAt(ind)))
				n = n*10 + a.charAt(ind) - '0';
			else if(a.charAt(ind)=='[')
			{
				tracking = true;
				fb = ind+1;
			}
			else if(a.charAt(ind)==']' && tracking)
			{
				tracking = false;
				String st = decompress(fb,ind);
				System.out.println(fb+" "+ind+" "+st);
				for(int i=0;i<n;i++)
					s += st;				
				n = 0;
				fb = ind+1;
			}	
			else if(!tracking)
				s += a.charAt(ind);
			ind++;
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
