#include<stdio.h>

long long int solve(long long int n) {
	if (n<5)
		return (1>n-1)?1:n-1;
	if (n%2||(n%4==0))
		return (n-solve(n-1));
	return (n-solve(n/2));
}

int main()
{
	int t, i, turn, coins;
	long long int n;
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		scanf("%lli", &n);
		printf("%lli\n", solve(n));
	}
	return 0;
}
