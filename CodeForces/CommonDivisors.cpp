#include<iostream>
using namespace std;

long long int get_factors(long long int n)
{
     if(n==1)
             return 1;
     long long int c = 0;
     for(int i=2;i<n;i++)
             if(n%i==0)
                       c++;
     return c+2;
}

int main()
{
	long n;
	cin>>n;
	long long int a[n];
	for(long i=0;i<n;i++)
	        cin>>a[i];
    sort(a, a+n);
    
    long long int ll = 0;
    long long int hl = n-1;
    while(a[ll]!=a[hl])
    {
            long c_0 = 0;
            for(long i = ll; i<hl; i++)
            {
                     a[i] = a[i+1]-a[i];
                     if(a[i]==0)  c_0++;
            }
            ll = c_0;
            hl--;
            sort(a,a+hl);
    }
                      
    long long int f = a[ll];
    for(long long int div=1; div<=f; div++)
    {
             long long divisor = (long long int)(f/div); 
             int flag =1;
             for(long i=0; i<n-1;i++)
             {
                 if(a[i]%divisor!=0)
                 {
                     flag = 0;
                     break;
                 }
             }
             if(flag==1)  
             {
                 f = divisor;
                 break;
             }
    }
             
	long long int c = get_factors(f);
	cout<<c<<endl;

	return 0;
}
