#include <iostream>
#include <string>
#include <vector>

using namespace std;

int findGroup(string s) {
    int len = s.length();
    string temp(1, s[0]);
    if (len == 1)
        return 1;
    for (int i = 1; i < len; ++i) {
        if (s[i - 1] != s[i]) {
            if (temp.find(s[i]) != string::npos) {
                return 0;
            } else {
                temp += s[i - 1];
            }            
        }
    }
    return 1;
}

int main() {
    int count = 0;
    int ret = 0;
    cin >> count;
    for (int i = 0; i < count; ++i) {
        string k;
        cin >> k;
        ret += findGroup(k);
    }
    cout << ret << endl;
    return 0;
}