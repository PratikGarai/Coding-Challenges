#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int k,n,t;
	long long int s1,s2,s, res;
	
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    s1 = 0;
	    s2 = 0;
	    s = 0;
	    res = 0;
	    cin>>n;
	    cin>>k;
	    int* arr = new int[n];
	    
	    for(int j=0;j<n;j++)
	    {
	        cin>>arr[j];
	        s += arr[j];
	    }
	    
	    sort(arr, arr+n);
	    for(int j=0;j<k;j++)
	    {
	        s1 += arr[j];
	    }
	    
	    for(int j=0;j<n-k;j++)
	    {
	        s2 += arr[j];
	    }
	    
	    s1 = s1<(s-s1)?s1:(s-s1);
	    s2 = s2<(s-s2)?s2:(s-s2);
	    
	    res = s2<s1?(s-2*s2):(s-2*s1);
	    
	    cout<<res<<endl;
	    
	}
	
	return 0;
}
