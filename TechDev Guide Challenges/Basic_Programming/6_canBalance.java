import java.util.Scanner;

class CanBalance
{

	public boolean canBalance(int[] nums) 
	{
  		int t_sum = 0;
  		for(int s : nums)
    			t_sum += s;
  		if(t_sum%2!=0)
    			return false;  
  		t_sum = t_sum/2;
  		for(int s : nums)
  		{
    			t_sum -= s;
    			if(t_sum==0)
      				return true;
    			if(t_sum<0)
      				return false;
  		}
  		return false;
	}

	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		CanBalance ob = new CanBalance();

		System.out.print("Enter the number of elements : ");
		int n = in.nextInt();
		int nums[] = new int[n];
		for(int i=0;i<n;i++)
		{
			System.out.print("Enter the "+(i+1)+"th element : ");
			nums[i] = in.nextInt();
		}
		
		if(ob.canBalance(nums))
			System.out.println("\nThe array is balanceable");
		else
			System.out.println("\nThe array is not balanceable");
	}
}
