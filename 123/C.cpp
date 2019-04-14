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
using namespace std;
int main(){
  ll n;
  std::vector<ll> traffic_time(5);
  cin>>n;
  for(int i=0;i<5;i++){
    cin>>traffic_time[i];
  }
  sort(traffic_time.begin(),traffic_time.end());
  ll ans;
  ans = floor(n/traffic_time[0])+5;
  cout<<ans<<endl;
  return 0;
}
