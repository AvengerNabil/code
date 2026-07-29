//https://codeforces.com/problemset/problem/268/B
#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;

    long long ans = n;

    for (long long i = 1; i < n; i++) {
        ans += i * (n - i);
    }

    cout << ans << '\n';

    return 0;
}
