import java.util.Map;
import java.util.HashMap;
import java.util.Scanner;

class MapShare
{
	public Map<String, String> mapShare(Map<String, String> map) 
	{
  		if(map.containsKey("a"))
  		{
    			map.put("b", map.get("a"));
  		}
  		if(map.containsKey("c"))
  		{
    			map.remove("c");
  		}
  		return map;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		MapShare ob = new MapShare();
		System.out.print("Enter the number of entries : ");
		int n = in.nextInt();
		Map<String, String> map = new HashMap<>();
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the key : ");
			String a = in.next();
			System.out.print("Enter the value : ");
			String b = in.next();
			map.put(a,b);
		}

		System.out.println("\nThe new map is : ");
		Map<String, String> new_map = ob.mapShare(map);
		for(Map.Entry<String,String> entry : map.entrySet())
			System.out.println(entry.getKey()+" -> "+entry.getValue());
	}
}
