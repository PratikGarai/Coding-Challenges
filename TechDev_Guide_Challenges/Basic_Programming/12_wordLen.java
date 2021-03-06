import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Word_Len
{
	public Map<String, Integer> word0(String[] strings) 
	{
  		Map<String , Integer> a = new HashMap<String, Integer>();
  		for(String s : strings)
    			a.put(s,s.length());
  		return a;
	}

	public static void main(String[] args)
	{
		Word_Len ob = new Word_Len();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of elements : ");
		int n = in.nextInt();
		String a[] = new String[n];
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the "+(i+1)+"th string : ");
			a[i] = in.next();
		}

		Map<String, Integer> map = ob.word0(a);
		System.out.println("-------------------------\nThe values :\n"); 
		for (Map.Entry<String,Integer> entry : map.entrySet()) 
		{
    			String key = entry.getKey();
    			int value = entry.getValue();
			System.out.println(key+"  -->  "+value);
		}
	}
}
