#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    int line = 0;
    int maxIdx = 0;
    int gap = 0;
    while (maxIdx < n) {
        ++line;
        maxIdx += line;
    }
    gap = maxIdx - n;
    if (line % 2 == 0) {
        cout << line - gap << '/' << gap + 1 << endl;
    } else {
        cout << gap + 1 << '/' << line - gap << endl;
    }
    return 0;
}