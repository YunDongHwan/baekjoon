#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int main() {
    vector<int> a = {1, 1, 2, 2, 2, 8};
    vector<int>::iterator i = a.begin();
    int c;
    for (; i != a.end(); i++) {
        cin >> c;
        cout << *i - c << " ";
    }
    return 0;
}