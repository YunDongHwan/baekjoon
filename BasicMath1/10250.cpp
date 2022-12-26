#include <iostream>
#include <string>

using namespace std;

int main() {
    int t, h, w, n;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> h >> w >> n;
        int hr = n % h;
        int wr = n / h + 1;
        if (hr == 0) {
            hr = h;
            wr -= 1;
        }
        cout << hr;        
        if (wr < 10) {
            cout << '0' << wr << endl;
        } else {
            cout << wr << endl;
        }
    }
    return 0;
}