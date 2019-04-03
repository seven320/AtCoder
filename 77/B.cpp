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
  ll N;
  cin>>N;

  ll ans = 0;
  for(int i=0;i<pow(10,5);i++){
    if(i*i>N){
      ans = pow((i-1),2);
      break;
    }
  }
  cout<<ans<<endl;
  return 0;
}
