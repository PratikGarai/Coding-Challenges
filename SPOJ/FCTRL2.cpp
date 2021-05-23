#include <bits/stdc++.h>
using namespace std;

int arr[25000];
int l = 25000;
int jump = 200;

void filler() {
    for(int i=0;i<l;i++)
        arr[i] = 0;
    
    arr[jump-1] = 1;
}

void fact(int i) {
    int beg = (i+1)*jump - 1;
    int pred = i*jump - 1;
    int lim = pred-jump;
    int carry = 0, val = 0;
    
    while(pred>lim) {
        val = arr[pred]*i + carry;
        carry = val/10;
        val = val%10;
        arr[beg] = val;
        pred--;
        beg--;
    }
}

void printer(int n) {
    int beg = n*jump;
    while(arr[beg]==0 && beg<(n+1)*jump)
        beg++;

    for(int i=beg;i<(n+1)*jump;i++) {
        cout<<arr[i];
    }
    
    cout<<"\n";
}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    filler();
    for(int i=1;i<=100;i++)
        fact(i);
    
    int t,n;
    cin>>t;
    while(t--){
        cin>>n;
        printer(n);
    }
    
    return 0;
}
