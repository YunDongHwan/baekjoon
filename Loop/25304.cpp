#include <iostream>

using namespace std;

int main() {
    int total_amount = 0;
    int kind = 0;
    int check_sum = 0;

    cin >> total_amount >> kind;

    for (int i = 0; i < kind; ++i) {
        int f = 0;
        int s = 0;
        cin >> f >> s;
        check_sum += f * s;
    }
    if (total_amount == check_sum)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
}