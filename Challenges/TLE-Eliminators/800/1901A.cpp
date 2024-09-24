#include<iostream>
using namespace std;

int max(int a, int b) {
    return a > b ? a:b;
}

int main() {
    int t;
    cin >> t;

    int n, x, i, mx;
    int *a;

    while(t--) {
        cin >> n >> x;
        a = new int[n];

        mx = 0;
        for(i = 0; i < n; i++) {
            cin >> a[i];
        }

        for(i = 0; i < n-1; i++) {
            mx = max(mx, a[i+1]-a[i]);
        }

        mx = max(mx, a[0]);
        mx = max(mx, 2*(x - a[n-1]));

        cout << mx << endl;
    }

    delete[] a;
    return 0;
}