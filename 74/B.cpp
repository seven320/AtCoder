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
  int N,K;
  cin>>N>>K;
  vector<int> x(N);
  for(int i=0;i<N;i++){
    cin>>x[i];
  }
  int ans = 0;
  for(int i=0;i<N;i++){
    ans += min(x[i],abs(x[i]-K))*2;
  }
  cout<<ans<<endl;
  return 0;
}
