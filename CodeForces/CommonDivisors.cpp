#include<iostream>
using namespace std;

long long int gcd(long long int a, long long int b)
{
	if(a==0)
		return b;
	return gcd(b%a, a);
}

int main()
{
	long n;
	cin>>n;
	long long int a[n];
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}

	long long int g = a[0];
	for(long i=1;i<n;i++)
		g = gcd(g, a[i]);

	long long int c=0;
	for(long long int j=1;j<=g;j++)
		if(g%j==0)
			c++;
	cout<<c<<endl;
	return 0;
}
