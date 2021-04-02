
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {

    int t, n, diff;
    
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        int* arr = (int*)malloc(n*sizeof(int));
        
        for(int j=0;j<n;j++)
            cin>>arr[j];
            
        sort(arr, arr+n);
        
        diff = arr[n-1]-arr[0];
        for(int j=1;j<n;j++)
        {
            diff = ((arr[j]-arr[j-1])<diff)?(arr[j]-arr[j-1]):diff;
        }
            
        cout<<diff<<endl;
    }
	return 0;
}
