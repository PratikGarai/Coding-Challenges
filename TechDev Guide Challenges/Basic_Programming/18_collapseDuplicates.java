import java.util.Scanner;

public class CollapseDup
{
	public String collapseDuplicates(String a) 
	{
  		if(a.length()<=1)
    			return a;
  		int i = 0; 
  		String result = ""; 
  		char ch = 'a';
  		while (i < (a.length()-1))
  		{ 
    			ch = a.charAt(i); 
    			result += ch; 
    			while (a.charAt(i+1) == ch && i < (a.length()-2)) 
      				i++; 
    			i++; 
  		} 
  		if(!(ch==a.charAt(a.length()-1)))
    			result += a.charAt(a.length()-1);
  		return result;
	}

	public static void main(String[] args)
	{
		CollapseDup ob = new CollapseDup();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the string to collapse : ");
		String s = in.next();
		System.out.print("The collapsed string : "+ob.collapseDuplicates(s));
	}
}
