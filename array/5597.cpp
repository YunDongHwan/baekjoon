#include <iostream>
#include <map>

using namespace std;

int main() {
    int arr[30] = {};
    int value = 0;
    for (int i = 0; i < 28; i++)
    {
        cin >> value;
        arr[value - 1] = value;
    }
    for (int i = 0; i < 30; i++)
    {
        if (arr[i] == 0)
            cout << i + 1 << endl;
    }
    return 0;
}
