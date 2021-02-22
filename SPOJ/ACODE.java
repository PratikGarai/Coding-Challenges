import java.util.*;
import java.lang.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner(System.in);
		int n,x1,x2,x;
		String s;
		long[] dp;
		
		while(true)
		{
			s = in.next();
			if(s.charAt(0)=='0')
				break;

			n = s.length();
			dp = new long[n+1];
			dp[0] = dp[1] = 1;
			for(int i=1;i<n;i++)
			{
				dp[i+1] = 0;

				x1 = s.charAt(i-1)-'0';	
				x2 = s.charAt(i)-'0';

				if(x2!=0)
					dp[i+1] += dp[i];

				x = x1*10+x2;
				if(x>=10 && x<=26)
					dp[i+1] += dp[i-1];
			}
			System.out.println(dp[n]);
		}

	}
}
