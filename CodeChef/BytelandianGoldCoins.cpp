#include <iostream>
#include <unordered_map>
using namespace std;
typedef long long int lli;
unordered_map<lli, lli> map;

lli process(lli n)
{
    if(n==0)
        return 0;
        
    if(map.find(n)!=map.end())
        return map[n];
    
    lli a,b,c;
    a = process(n/2);
    b = process(n/3);
    c = process(n/4);
    
    map[n] = n>(a+b+c)?n:(a+b+c);
    
    return map[n];
}

int main() {
	lli n;
	while(cin>>n)
	    cout<<process(n)<<endl;
	    
	return 0;
}
