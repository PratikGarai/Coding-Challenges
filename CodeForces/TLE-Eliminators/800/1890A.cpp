#include<iostream>
#include<map>
using namespace std;

void solve() {
    int n, i;
    int* arr;

    cin >> n;
    arr = new int[n];
    for(i = 0; i < n; i++) {
        cin >> arr[i];
    }

    map<int, int> mp;
    for(i = 0; i < n; i++) {
        if (mp.find(arr[i]) != mp.end()) {
            mp[arr[i]]++;
        } else {
            mp[arr[i]] = 1;
        }
    }

    if(mp.size() > 2) {
        cout << "No" << endl;
        return;
    }

    if(mp.size() == 1) {
        cout << "Yes" << endl;
        return;
    }

    int n1, n2;
    i = 0;
    for(const auto& pair : mp) {
        if(i == 0) {
            i++;
            n1 = pair.second;
        } else {
            n2 = pair.second;
        }
    }

    if(n1-n2 == -1 || n1-n2 == 1 || n1 == n2) {
        cout << "Yes" << endl;
        return;
    } else {
        cout << "No" << endl;
        return;
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