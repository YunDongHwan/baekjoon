#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    stoi(a);
    stoi(b);

    cout << max(a, b) << endl;
    return 0;
}