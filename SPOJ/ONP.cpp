#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void process() {
    char e[400], p[400];
    cin>>e;
    
    stack<char> stck;
    
    int p1 = 0;
    int p2 = 0;
    int l = strlen(e);
    
    for(int i=0;i<l;i++)
    {
        if(e[i]>='a' && e[i]<='z')
            cout<<e[i];
        else if(e[i]==')')
        {
            cout<<stck.top();
            stck.pop();
        }
        else if(e[i]!='(') 
        {
            stck.push(e[i]);
        }
    }
    
    while(!stck.empty())
    {
        cout<<stck.top();
        stck.pop();
    }
    
    cout<<"\n";
}

int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int t;
	cin>>t;
	while(t--)
	    process();
	
	return 0;
}
