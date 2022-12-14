#include <iostream>
#include <string>

using namespace std;

int main() {
    int N = 0;
    int line = 0;
    cin >> N;    
    int temp  = 1;
    int i = 0;
    if (N == 1) {
        cout << 1 << endl;
        return 0;
    }
    for (; temp < N; ++i) {
        temp += (i * 6);
    }
    cout << i << endl;
    return 0;
}