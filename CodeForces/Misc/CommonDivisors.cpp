#include<iostream>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b)
{
	if(a==0)
		return b;
	gcd(b%a, a);
}

int main()
{
	ll n, i;
	cin>>n;
	ll a[n];
	ll g=0;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
		g = gcd(g,a[i]);
	}
	
	ll f_c = 0;
	for(i=1;i*i<g;i++)
	{
		if(g%i) continue;
		else f_c += 2;
	}
	if(g==i*i) f_c +=1 ;
	cout<<f_c<<endl;
	
	return 0;
}
