#include<stdio.h>
int main()
{
	int t, i, n, turn, coins;
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		scanf("%d", &n);
		turn = 1;
		coins = 0;
		while(n>0)
		{
			if(turn)
			{
				if((n%4==0&&n>=8)||n%2==1)
				{
					coins+=1;
					n--;
				}
				else
				{
					coins+=n/2;
					n=n/2;
				}
				turn = 0;
			}
			else
			{
				if(n%2==0)
					n=n/2;
				else
					n--;
				turn = 1;
			}
		}
		printf("%d\n", coins);
	}
	return 0;
}
