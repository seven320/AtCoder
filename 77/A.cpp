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
// int inf = INFINITY;
int main(){

  string C1,C2;

  bool ans = true;
  cin>>C1>>C2;
  if(C1[0]==C2[2] && C1[1]==C2[1] && C1[2]==C2[0]){
    ans = true;
  }
  else{
    ans = false;
  }
  if(ans){
    cout<<"YES"<<endl;
  }
  else{
    cout<<"NO"<<endl;
  }
  return 0;
}
