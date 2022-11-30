#include <iostream>
#include <string>

using namespace std;

int main() {
    int count = 0;
    string all = "";
    int sum = 0;

    cin >> count >> all;
    for (int i = 0; i < count; ++i) {
        const char k = all[i];
        sum += atoi(&k);
    }

    cout << sum << endl;
    return 0;
}