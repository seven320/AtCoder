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
  ll N,K;
  vector<ll> a(100000+1);
  cin>>N>>K;
  for(ll i=0;i<N;i++){
    cin>>a[i];
  }

  ll tmp = 0;
  vector<ll> part_sum(100001);
  for(int i=0;i<N;i++){
    tmp = tmp + a[i];
    part_sum[i+1] = tmp;
  }

  ll ans = 0;
  for(int i=N;i>=0;i--){
    if(part_sum[i] >= K){
      for(int j=i;j>=0;j--){
        // cout<<i<<" "<<j<<endl;
        // cout<<part_sum[i]<<part_sum[j]<<endl;
        if(part_sum[i]-part_sum[j] >= K){
          ans += j+1;
          break;
        }
      }
    }
    else{
      break;
    }
  }
  cout<<ans<<endl;
  return 0;
}
