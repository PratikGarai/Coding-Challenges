import java.util.Scanner;

class StringSplosion
{
	String stringSplosion(String str) 
	{
  		String s = "";
  		for(int i=0;i<str.length();i++)
    			s += str.substring(0,i+1);
  		return s;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		StringSplosion ob = new StringSplosion();
		String s, res;
		System.out.print("Enter the string : ");
		s = in.next();
		res = ob.stringSplosion(s);
		System.out.println("The result : "+res);
	}
}
