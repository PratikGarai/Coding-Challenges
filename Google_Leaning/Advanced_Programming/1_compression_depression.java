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
		int m_ind = f;
		String s = "";
		while(m_ind <= l)
		{
			if(Character.isDigit(a.charAt(m_ind)))
			{
				int ind = m_ind;
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
				m_ind = ind;
				String st = decompress(begin, end);
				for(int i=0;i<n;i++)
					s += st;
			}
			else
			{
				int ind = m_ind;
				int begin = m_ind;
				while(ind<=l)
				{
					char c = a.charAt(ind);
					if( (c>=65 && c<=90)||(c>=97 && c<=122)) 
						ind++;
				}
				int end = ind-1;
				m_ind = ind;
				s += a.substring(begin, end+1);
			}
		}
		return s;
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
