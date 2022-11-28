#include <iostream>
#include <string>

using namespace std;

int main() {
    int count = 0;
    int target = 0;

    cin >> count;
    int all_num[count];
    int tc = 0;
    for (int i = 0; i < count; i++)
    {
        cin >> all_num[i];
    }

    cin >> target;

    for (int i = 0; i < count; i++)
    {
        if (all_num[i] == target)
            tc++;
    }
    cout << tc << endl;
    return tc;
}