//encoding:utf-8
//#include <iostream> //c++
//#include<stack> //スタックに関して　最新のデータから捨てる
//#include<queue> //キューに関して　最古のデータから捨てる
//#include<math.h>
//#include<vector>
//#include<algorithm> //sort とかにいる
#include<bits/stdc++.h>//vector,algorithm,que
#include<time.h> //時間にかんして

#define ll long long
#define MOD 1000000007
#define INF (1<<29)
using namespace std;
int main(){
  ll N;
  ll ag,as,ab;
  ll bg,bs,bb;
  cin >> N;
  cin>>ag>>as>>ab;
  cin>>bg>>bs>>bb;
  vector<ll> dp(N+1);
  ll g_v = bg-ag;
  ll s_v = bs - as;
  ll b_v = bb - ab;
  if(g_v>0){
    for(int i=ag;i<N+1;i++){
      dp[i] = max(dp[i],dp[i-ag]+g_v);
    }
  }
  if(s_v>0){
    for(int i=as;i<N+1;i++){
      dp[i] = max(dp[i],dp[i-as]+s_v);
    }
  }
  if(b_v>0){
    for(int i=ab;i<N+1;i++){
      dp[i] = max(dp[i],dp[i-ab]+b_v);
    }
  }
  ll tmp = 0;
  for(int i=0;i<N+1;i++){
    tmp = max(tmp,dp[i]);
  }
  ll M = N+tmp;
  vector<ll> dp2(M+1);
  g_v = -bg + ag;
  s_v = -bs + as;
  b_v = -bb + ab;

  if(g_v>0){
    for(int i=bg;i<M+1;i++){
      dp[i] = max(dp2[i],dp2[i-bg]+g_v);
    }
  }
  if(s_v>0){
    for(int i=bs;i<M+1;i++){
      dp[i] = max(dp2[i],dp2[i-bs]+s_v);
    }
  }
  if(b_v>0){
    for(int i=bb;i<M+1;i++){
      dp[i] = max(dp2[i],dp2[i-bb]+b_v);
    }
  }
  tmp = 0;
  for(int i=0;i<M+1;i++){
    tmp = max(tmp,dp2[i]);
  }
  ll ans = M+tmp;
  cout<<ans<<endl;

  return 0;
}
