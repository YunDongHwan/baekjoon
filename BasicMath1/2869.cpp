#include <iostream>
#include <string>

using namespace std;

int main() {
    int v = 0, a = 0, b = 0;
    cin >> a >> b >> v;
    int up = a - b;
    int i = (v - a) / up;
    if (i * up + a >= v) {
        ++i;
    } else if (v - a % up > 0 ) {
        i += 2;
    }
    cout << i << endl;
    return 0;
}