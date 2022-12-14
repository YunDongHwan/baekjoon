#include <iostream>
#include <string>

using namespace std;

int main() {
    unsigned int A = 0, B = 0, C = 0;
    cin >> A >> B >> C;
    int profit = C - B;
    unsigned int count = 0;
    if (profit <= 0) {
        cout << -1 << endl;
        return 0;
    } else {
        count = A / profit;
    }
    cout << count + 1 << endl;
    return 0;
}