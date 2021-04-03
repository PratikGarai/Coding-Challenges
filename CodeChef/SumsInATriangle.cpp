#include <iostream>
using namespace std;

void process()
{
    int n;
    cin>>n;
    
    int *m = (int*)malloc(n*n*sizeof(int));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<i+1;j++)
        {
            cin>>m[i*n+j];
        }
        for(int j=i+1;j<n;j++)
        {
            m[i*n+j] = 0;
        }
    }
    
    int ind = n-2;
    while(ind>=0)
    {
        for(int j=0;j<n;j++)
        {
            m[ind*n+j] += m[(ind+1)*n+j]>m[(ind+1)*n+j+1]?m[(ind+1)*n+j]:m[(ind+1)*n+j+1];
        }
        ind--;
    }
    
    cout<<m[0]<<endl;
}


int main() {
	
	int t;
	cin>>t;
	while(t--)
	    process();
	
	return 0;
}
