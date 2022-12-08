#include <iostream>
#include <string>
#include <array>

using namespace std;

int main() {
    string s;
    cin >> s;
    string arr[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int len = sizeof(arr) / sizeof(arr[0]);
    int count = 0;
    for (int i = 0; i < len; ++i) {
        while (1) {
            int idx = s.find(arr[i]);
            if (idx != string::npos ) {
                s.replace(idx, arr[i].length(), "*");
            } else {
                break ;
            }
        }  
    }
    cout << s.length() << endl;
    return 0;
}