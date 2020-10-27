import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Encoder
{
	public String[] encoder(String[] raw, String[] code_words) 
	{
  		Map<String, String> a = new HashMap<String, String>();
  		int ind = 0;
  		for(String s : raw)
    			if(!a.containsKey(s))
      				a.put(s,code_words[ind++]);
  
  		String res[] = new String[raw.length];
  		ind = 0;
  		for(String s : raw)
    			res[ind++] = a.get(s);
  		return res;
	}

	public static void main(String[] args)
	{
		Encoder ob = new Encoder();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of raw data : ");
		int m = in.nextInt();
		System.out.print("Enter the number codes : ");
		int n = in.nextInt();
		String r[] = new String[m];
		String c[] = new String[n];
		for(int i=0;i<m;i++)
		{
			System.out.print("Enter the "+(i+1)+"th raw data : ");
			r[i] = in.next();
		}
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the "+(i+1)+"th code : ");
			c[i] = in.next();
		}

		String res[] = ob.encoder(r,c);
		System.out.println("Result : ");
		for(String s : res)
			System.out.print(s+"\t");
	}
}
