#include <iostream>
#include <algorithm>

using namespace std;

int checkSame(int * arr, int &same) {
    int num = 0;
    if (arr[0] == arr[1]) {
        (same)++;
        num = arr[0];
        if (arr[0] == arr[2]) {
            (same)++;
            num = arr[0];
        }
    }
    else if (arr[1] == arr[2]) {
        (same)++;
        num = arr[1];
    }
    return num;
}

int main() {
    int max = 0;
    int a[3];
    int same_count = 0;

    for(int i = 0; i < 3; i++) {
        cin >> a[i];
        max = max > a[i] ? max : a[i];
    }
    sort(a, a+3);
    int snum = checkSame(a, same_count);
    if (same_count == 2) {
        cout << 10000 + snum * 1000 << endl;
    } else if (same_count == 1) {
        cout << 1000 + snum * 100 << endl;
    } else {
        cout << max * 100 << endl;
    }
    return 0;
}