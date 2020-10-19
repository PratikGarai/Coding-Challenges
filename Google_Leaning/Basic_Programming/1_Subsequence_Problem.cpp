// Given a string 'S' and a set of words 'D' , find all 
// words in 'D' that are subsequence of 'S'

#include<iostream>
using namespace std;

string S;
string* D;

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
	for(i=0;i<l;i++)
	{
		cout<<"Enter the length of "<<i+1<<"th word : ";
		cin>>l_w;
		cout<<"Enter the word : ";
		cin>>D[i];
	}
	cout<<"\nMain word : "<<S<<endl;
	for(i=0;i<l;i++)
		cout<<i+1<<"th word : "<<D[i]<<endl;

	return 0;
}
