#include <bits/stdc++.h>
#include <cmath>
using namespace std;

typedef long long ll;

int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	ll l = 32000;
    	int arr[l];
    	ll pcount = 0;
    	int primes[16000];
	
	for(ll i=0;i<l;i++)
	{
		arr[i] = 1;
	}
	
	arr[0] = 0;
	arr[1] = 0;
	arr[2] = 1;
	for(ll i=0;i<(ll)sqrt(l)+1;i++)
	{
		if(arr[i]==0)
			continue;
		ll j=2;
		while((i*j)<l)
		{
			arr[i*j] = 0;
			j++;
		}
	}
	
	for(ll i=0;i<l;i++)
	{
		if(arr[i]==1)
		{
			primes[pcount++] = i;
		}
	}
	
	
	int t;
	cin>>t;
	while(t--)
	{
		int m, n;
    	cin>>m>>n;
    	for(int i=m;i<=n;i++)
    	{
    		int prime = 1;
    		for(int j=0; j<pcount; j++)
    		{
    			if(i%primes[j]==0 && i!=primes[j])
    			{
    				prime = 0;
    				break;
    			}
    		}
    		
    		if(prime==1 && i!=1)
    			cout<<i<<"\n";
    	}
    	cout<<"\n";
	}
	
	return 0;
}
