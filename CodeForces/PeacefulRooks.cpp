#include<iostream>
using namespace std;

void process()
{
	int n, m, ans=0;
	cin>>n;
	cin>>m;
	
	int x,y;
	int row_occupant[n], mx[m], my[m];
	for(int i=0;i<n;i++)
	{
		row_occupant = -1;
	}

	for(int i=0;i<m;i++)
	{
		cin>>x;
		cin>>y;
		mx[i] = x-1;
		my[i] = y-1;
		row_occupant[x-1] = i;
	}

	cout<<"Result : ";
	cout<<ans<<endl;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
		process();
	return 0;
}
