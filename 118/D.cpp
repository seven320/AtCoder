//encoding:utf-8
#include<iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる
#include<string>
#include <unordered_set>//c++11に必要

#define ll long long
using namespace std;
int main(){
  int N,M;
  cin>>N>>M;
  vector<int>can(M);
  for(int i=0;i<M;i++){
    cin>>can[i];
  }
  sort(can.rbegin(),can.rend());
  // vector<int> sticks{0, 2, 5, 5, 4, 5, 6, 3, 7, 6};

  vector<int> sticks{0,2,5,5,4,5,6,3,7,6};


  vector<int>dp(N+1);
  for(int i=1;i<N+1;i++){
    dp[i]=-1;
  }
  dp[0]=0;
  for(int i=1;i<N+1;i++){
    for (auto x:can){
      if(i>=sticks[x]){
        dp[i] = max(dp[i],dp[i-sticks[x]]+1);
      }
    }
  }


  // 一回何桁まで行けるかをｄｐでといた後に復元する
  // 最大桁までいけたパターンから後ろ向きに調べて行く
  int remain = N;
  while(remain>0){
    for(auto x:can){
      if(dp[remain-sticks[x]]==dp[remain]-1){
        if(dp[remain-sticks[x]]>0 || remain-sticks[x]==0){
          remain -= sticks[x];
          cout<<x;
          break;
        }
      }
    }
  }
  // while (remain > 0) {
  //   // cout<<remain<<endl;
  //     for (auto x:can) {
  //         if (dp[remain - sticks[x]] == dp[remain] - 1)
  //             if (dp[remain - sticks[x]] > 0 || remain - sticks[x] == 0) {
  //                 remain -= sticks[x];
  //                 cout << x;
  //                 break;
  //             }
  //     }
  // }

  cout<<endl;

  return 0;
}
