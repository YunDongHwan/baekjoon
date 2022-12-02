#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

int main() {
    string S = "";
    int len = 0;
    int target = 0;
    cin >> S;
    len = S.length();
    for (char i = 'a'; i <= 'z'; ++i) {
        target = S.find(i);
        if (string::npos == target) {
            cout << -1 << endl;
        } else {
            cout << target << endl;
        }
    }
    return (0);
}