#include<iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    int n, k, i, last;
    int* a;
    bool isSorted;

    while(t--) {
        cin>> n >> k;
        isSorted = true;
        a = new int[n];

        for(i=0; i<n; i++) {
            cin>>a[i];
        }

        last = a[0];
        for(i=0; i<n; i++) {
            if(a[i] >= last) {
                last = a[i];
            } else {
                isSorted = false;
                break;
            }
        }

        if(isSorted) {
            cout<<"YES\n";
            continue;
        }

        if (k > 1) {
            cout<<"YES\n";
        } else {
            cout<<"NO\n";
        }

        delete[] a ;
    }


    return 0;
}