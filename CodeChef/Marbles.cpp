#include <iostream>
using namespace std;

typedef long long int lli;

void process() {
    lli n, k;
    cin>>n>>k;
    lli res = 1;
    for(lli i=1;i<k;i++)
    {
        res = res*(n-k+i)/i;
    }
    
    cout<<res<<endl;
}

int main() {
	int t;
	cin>>t;
	while(t--)
	    process();
	return 0;
}
