//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる


// #include <bits/stdc++.h>
using namespace std;
int main() {
int N, M; cin >> N >> M; vector<int> cnt(M, 0);
for (int i = 0; i < N; ++i) {
int K; cin >> K;
for (int j = 0; j < K; ++j) {
int A; cin >> A; --A;
 ++cnt[A]; }
}
int ans = 0; for (int i =
if (cnt[i] ++ans;
} }
0; i < M; ++i) { == N) {
cout << ans << endl; }
