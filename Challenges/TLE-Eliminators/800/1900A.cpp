#include<iostream>
#include<cstring>
using namespace std;

int main() {
    int t;
    cin >> t;

    int n, i, cont, ans;
    string s;

    while(t--) {
        cin >> n;
        cin >> s;

        cont = 0;
        ans = 0;

        for(i = 0; i < n; i++) {
            if(s[i] == '.') {
                cont++;
            } else {
                if(cont >= 3) {
                    ans = 2;
                    break;
                } else {
                    ans += cont;
                }
                cont = 0;
            }
        }
        if(cont >= 3)
            ans = 2;
        else 
            ans += cont;
        cout << ans << endl;
    }

    return 0;
}