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
  ll X,t;
  cin>>X>>t;
  ll ans=0;
  if(X-t<0)ans = 0;
  else ans = X-t;
  // ans = max(0,X-t);
  cout<<ans<<endl;
  return 0;
}
