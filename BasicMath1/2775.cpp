#include <iostream>
#include <string>

using namespace std;

int getPeople(int k, int n) {
    if (n == 0)
        return 1;
    else if (k == 0) {        
        return n; 
    }
    return (getPeople(k - 1, n) + getPeople(k, n - 1));
}

int main() {
    int t, k, n;
    cin >> t;
    while (t--) {
        int p = 1;
        cin >> k >> n;
        cout << getPeople(k, n) << endl;
    }
    return 0;
}