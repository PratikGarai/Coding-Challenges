// Given a string 'S' and a set of words 'D', find number
// of words in 'D' that are subsequence of 'S' with max length.

#include<iostream>
using namespace std;

string S;
string* D;
int* lengths;

int calculate(int l, int l_s)
{
	int i,j,max_len=0,n_max=0;
	int index[l];
	for(i=0;i<l;i++)
		index[i] = 0;
	for(i=0;i<l_s;i++)
	{
		for(j=0;j<l;j++)
		{
			if(index[j]<lengths[j])
			{
				if(D[j][index[j]]==S[i])
					index[j]++;
			}
		}
	}
	
	for(i=0;i<l;i++)
	{
		if(index[i]==max_len && index[i]==lengths[i])
			n_max++;
		else if(index[i]>max_len && index[i]==lengths[i])
		{
			max_len = index[i];
			n_max = 1;
		}
	}
	return n_max;
}

int main()
{
	int l,l_s,l_w,i;
	cout<<"Enter the length of 'S' : ";
	cin>>l_s;
	cout<<"Enter 'S' : ";
	cin>>S;
	cout<<"Enter the number of words : ";
	cin>>l;
	D = new string[l];
	lengths = new int[l];
	for(i=0;i<l;i++)
	{
		cout<<"Enter the length of "<<i+1<<"th word : ";
		cin>>l_w;
		cout<<"Enter the word : ";
		cin>>D[i];
		lengths[i] = l_w;
	}
	/* cout<<"\nMain word : "<<S<<endl; */
	/* for(i=0;i<l;i++) */
	/* 	cout<<i+1<<"th word : "<<D[i]<<endl; */

	cout<<"\nNumber of max length substrings : "<<calculate(l, l_s)<<endl;

	return 0;
}
