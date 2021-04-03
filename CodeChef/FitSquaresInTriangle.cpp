
#include <iostream>
using namespace std;

void process() {
    int b;
    cin>>b;
    
    b -= 2;
    int c = 0;
    
    b -= b%2;
    b = b/2;
    c = b*(b+1)/2;
    cout<<c<<endl;
}


int main() {
	int t;
	cin>>t;
	while(t--)
	    process();
	return 0;
}
