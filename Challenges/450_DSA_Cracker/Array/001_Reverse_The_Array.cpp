#include <bits/stdc++.h> 
typedef long long int lli;

void reverseArray(vector<int> &arr , int m)
{
	int beg = m + 1, end = arr.size() - 1;
	int mid = (beg + end) / 2; 
	lli a, b;
	
	for(int i = beg; i < mid + 1; i++) {
		a = arr[i];
		b = arr[end - (i-beg)];
		arr[i] = b;
		arr[end - (i-beg)] = a;
	}

	return;
}
