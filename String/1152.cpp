#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    string s;
    string temp;
    vector<string> v;

    getline(cin, s);
    
    stringstream ss(s);
    while (getline(ss, temp, ' ')) {
        if (temp != "") {
            v.push_back(temp);
        }
    }
    cout << v.size() << endl;
    return 0;
}