#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    int N, M;
    int num;
    int i, j;
    cin >> N >> M;
    vector<int> n(N + 1);
    n[0] = 0;
    for (int q = 0; q < N; ++q) {
        cin >> num;        
        n[q + 1] = n[q] + num;
    }
    while (M--) {
        cin >> i >> j;
        cout << n[j] - n[i - 1] << '\n';
    }
    return 0;
}