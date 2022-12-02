#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int howMany(string s, char c) {
    int count = 0;
    for (char a : s) {
        if (c == a)
            ++count;
    }
    return count;
}

int main() {
    string k;
    cin >> k;
    transform(k.begin(), k.end(), k.begin(), ::toupper);
    int ret = 0;
    int max = 0;
    char maxc = '\0';
    int check = 0;
    
    for (char i = 'A'; i <= 'Z'; ++i) {
        ret = howMany(k, i);
        if (max <= ret) {
            if (max == ret) {
                check = 1;
            } else {
                check = 0;
            }
            max = ret;
            maxc = i;
        }
    }
    if (check == 1) {
        cout << '?' << endl;
    } else {
        cout << maxc << endl;
    }
    return 0;
}