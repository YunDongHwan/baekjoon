#include <iostream>

using namespace std;

string newString(int r, string s) {
    string n;
    int len = s.length();
    for (int i = 0; i < len; ++i) {
        for (int j = 0; j < r; ++j) {
            n += s[i];
        }
    }
    return n;
}

int main() {
    int count;
    int repeat;
    string ret;
    string S;
    cin >> count;
    for (int i = 0; i < count; ++i) {
        cin >> repeat >> S;
        ret = newString(repeat, S);
        cout << ret << endl;
    }
    return (0);
}