#include<iostream>
using namespace std;

typedef long long int lli;

void process()
{
	int n;
	cin>>n;

	lli t[n+1], x[n+1];
	for(int i=0;i<n;i++)
	{
		cin>>t[i];
		cin>>x[i];
	}

	t[n+1] = 1000000000;

	lli current_start = 0;
	lli current_dest = 0;
	lli current_time = 0;
	lli current_speed = 0;
	lli future_time = 0;
	int success = 0;

	lli min, max;

	for(int i=0;i<n-1;i++)
	{
		/* cout<<"Processing : "<<t[i]+" "<<x[i]<<endl; */
		if(current_dest-current_start>t[i]-current_time)
		{
			min = current_start+current_speed*(t[i]-current_time);
			max = current_start+current_speed*(t[i+1]-current_time);

			if(current_speed>=0 && min<=x[i] && max>=x[i])
			{
				success++;
				/* cout<<"Method 1"<<endl; */
			}
			else if(current_speed<0 && min>=x[i] && max<=x[i])
			{
				success++;
				/* cout<<"Method 2"<<endl; */
			}
			continue;
		}

		cout<<"Accepting : "<<t[i]<<" "<<x[i]<<endl;

		current_start = current_dest;
		current_dest = x[i];
		current_time = t[i];

		if(current_dest<current_start)
			current_speed = -1;
		else if(current_start<current_dest)
			current_speed = 1;
		else 
			current_speed = 0;

		min = current_start+current_speed*(t[i]-current_time);
		max = current_start+current_speed*(t[i+1]-current_time);

		if(current_speed>=0 && min<=x[i] && max>=x[i])
		{
			success++;
			/* cout<<"Method 3"<<endl; */
		}
		else if(current_speed<0 && min>=x[i] && max<=x[i])
		{
			success++;
			/* cout<<"Method 4"<<endl; */
		}
	}

	if(current_speed<0 && current_dest>t[n])
		success++;
	else if(current_speed>0 && current_dest<t[n])
		success++;

	cout<<"Result : "<<success<<endl;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
		process();

	return 0;
}
