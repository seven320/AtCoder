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
  int x,y,z,k;
  cin>>x>>y>>z>>k;
  vector<ll> A(x),B(y),C(z);

  for(int i=0;i<x;i++){
    cin>>A[i];
  }
  for(int i=0;i<y;i++){
    cin>>B[i];
  }
  for(int i=0;i<x;i++){
    cin>>C[i];
  }

  vector<ll> ab;
  for(int i=0;i<x;i++){
    for(int j=0;j<y;j++){
      ab.push_back(A[i]+B[j]);
    }
  }
  sort(ab.begin(),ab.end());
  reverse(ab.begin(),ab.end());

  vector<ll> ans(k);
  for(int i=0;i<min(k,(int)ab.size());i++){
    for(int j=0;j<z;j++){
      ans.push_back(ab[i]+C[j]);
    }
  }
  sort(ans.begin(),ans.end());
  reverse(ans.begin(),ans.end());
  // cout<<ans.size()<<endl;
  for(int i=0;i<k;i++){
    cout<<ans[i]<<endl;
  }

  return 0;
}
