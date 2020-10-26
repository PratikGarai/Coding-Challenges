import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Word_Zero
{
	public Map<String, String> word0(String[] strings) 
	{
  		Map<String , String> a = new HashMap<String, String>();
  		for(String s : strings)
			a.put(String.valueOf(s.charAt(0)), String.valueOf(s.charAt(s.length()-1)));
  		return a;
	}

	public static void main(String[] args)
	{
		Word_Zero ob = new Word_Zero();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of elements : ");
		int n = in.nextInt();
		String a[] = new String[n];
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the "+(i+1)+"th string : ");
			a[i] = in.next();
		}

		Map<String, String> map = ob.word0(a);
		System.out.println("-------------------------\nThe values :\n"); 
		for (Map.Entry<String,String> entry : map.entrySet()) 
		{
    			String key = entry.getKey();
    			String value = entry.getValue();
			System.out.println(key+"  -->  "+value);
		}
	}
}
