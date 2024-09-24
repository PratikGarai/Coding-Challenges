#include<iostream>
using namespace std;

void solve() {
    int n, i;
    int* arr;

    cin >> n;
    arr = new int[n];
    for(i = 0; i < n; i++) {
        cin >> arr[i];
    }

    if (arr[0] == 1) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    delete[] arr;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        solve();
    }

    return 0;
}