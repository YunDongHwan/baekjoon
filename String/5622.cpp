#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int len = s.length();
    int time = 0;
    string except = "SVYZ";
    for (int i = 0; i < len; ++i) {
        time += ((s[i] - 'A') / 3) + 3;
        if (except.find(s[i]) != string::npos)
            time -= 1;
    }
    cout << time << endl;
    return 0;
}