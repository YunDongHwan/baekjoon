#include <iostream>
#include <numeric>
#include <iterator>

using namespace std;

int main() {
    int N;
    int arr[1001];
    int num;
    cin >> N;
    iota(begin(arr), end(arr), 0);
    arr[1] = 0;
    for (int i = 2; i <= 1000; ++i) {
        if (arr[i] != 0) {
            for (int j = i * 2; j <= 1000; j += i) {
                arr[j] = 0;
            }
        }
    }
    int answer = 0;
    for (int i = 0; i < N; ++i) {
        cin >> num;
        if (arr[num] != 0)
            answer++;
    }
    cout << answer << endl;
    return 0;
}