#include<iostream>
using namespace std;
typedef long long int lli;

void process()
{
	lli n;
	cin>>n;

	lli k;
	lli rem;
	int flag = 0;
	while(true)
	{
		k = n;
		while(k!=0)
		{
			rem = k%10;
			if(rem!=0)
			{
				if(n%rem!=0)
				{
					flag = 1;
					break;
				}
			}
			k = k/10;
		}
		if(flag==1)
		{
			flag = 0;
			n++;
		}
		else
		{
			/* cout<<"Result : "; */
			cout<<n<<endl;
			return;
		}
	}
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
		process();
}
