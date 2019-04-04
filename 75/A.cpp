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
  int a,b,c;
  cin>>a>>b>>c;
  int ans;
  if(a==b){
    ans = c;
  }
  else if(a==c){
    ans = b;
  }
  else{
    ans = a;
  }
  cout<<ans<<endl;

  return 0;
}
