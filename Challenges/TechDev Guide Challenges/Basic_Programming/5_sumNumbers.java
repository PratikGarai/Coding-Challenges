import java.util.Scanner;

class SumNumbers
{
	public int sumNumbers(String str) 
	{
  		int g_sum = 0, l_sum=0, diff;
  		boolean is_num = false;
  		for(int i=0;i<str.length();i++)
  		{
    			diff =  str.charAt(i)-'0';
    			if(diff>=0&&diff<=9)
    			{
      				l_sum = l_sum*10+diff;
      				if(!is_num)
        				is_num = true;
    			}
    			else if(is_num)
    			{
      				is_num = false;
      				g_sum += l_sum;
      				l_sum = 0;
    			}
  		}
  		if(is_num)
    			g_sum += l_sum;
  		return g_sum;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		SumNumbers ob = new SumNumbers();
		System.out.print("Enter the string : ");
		String a = in.nextLine();
		System.out.println("The sum : "+ob.sumNumbers(a));
	}	
}
