#include<iostream>
using namespace std;

void process()
{
	int n;
	cin>>n;
	char str[n];
	cin>>str;
	int count = 0;
	for(int i=n-1;i>=0;i--)
		if(str[i]!=')')
			break;
		else 
			count++;
	/* cout<<"Result :"<<count<<" "<<n; */
	if(count>n/2)
		cout<<"Yes"<<endl;
	else
		cout<<"No"<<endl;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
		process();
}
