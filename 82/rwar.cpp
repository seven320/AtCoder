
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> sticks{0, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    vector<int> can(m);
    for (int i = 0; i < m; i++) cin >> can[i];
    sort(can.begin(), can.end());
    reverse(can.begin(), can.end());

    vector<int> dp(n + 1);//dp[i]=i本でできる最大桁数
    for (int i = 1; i <= n; i++)dp[i] = -1145141919;
    for (int i = 1; i <= n; i++) {
        for (auto x:can) {
            if (i - sticks[x] >= 0)
                dp[i] = max(dp[i], dp[i - sticks[x]] + 1);
        }
    }
    // for(int i=0;i<n;i++){
    //   cout<<dp[i]<<endl;
    // }
    int remain = n;
    while (remain > 0) {
      cout<<remain<<endl;
        for (auto x:can) {
            if (dp[remain - sticks[x]] == dp[remain] - 1)
                if (dp[remain - sticks[x]] > 0 || remain - sticks[x] == 0) {
                    remain -= sticks[x];
                    cout << x;
                    break;
                }
        }
    }
    cout << endl;

    return 0;
}
