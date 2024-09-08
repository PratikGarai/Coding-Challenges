import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class SequenceTransformation
{
	static Scanner in = new Scanner(System.in);
	static int process(int n)
	{
		int[] arr = new int[n];
		for(int i=0;i<n;i++)
			arr[i] = in.nextInt();
		HashMap<Integer,Integer> h = new HashMap<Integer,Integer>(n);
		int last = arr[0];
		h.put(last,1);
		int c;
		for(int i=1;i<n;i++)
		{
			if(last==arr[i])
				continue;
			last = arr[i];
			c = h.getOrDefault(arr[i], -1);
			if(c==-1)
				h.put(arr[i],1);
			else
				h.put(arr[i],c+1);
		}
		
		int min = n+5;
		int min_ele = -1;
		for(Map.Entry<Integer, Integer> entry : h.entrySet())
		{
			if(entry.getValue()<min)
			{
				min_ele = entry.getKey();
				min = entry.getValue();
			}
		}

		if(arr[0]==arr[n-1])
			return Math.min(h.get(arr[0])-1, min+1);
		else if(arr[0]==min_ele) 
			return Math.min(min, h.get(arr[n-1]));
		else if(arr[n-1]==min_ele)
			return Math.min(min, h.get(arr[0]));
		return Math.min(h.get(arr[0]), Math.min(h.get(arr[n-1]), min+1));
	}

	public static void main(String[] args)
	{
		int t = in.nextInt();
		for(int i=0;i<t;i++)
		{
			int n = in.nextInt();
			System.out.println(process(n));
		}
	}
}
