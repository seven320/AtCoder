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
  ll R,G,B,N;
  cin>>R>>G>>B>>N;
  ll ans = 0;
  for(int i=0;i<(int)3000/R+1;i++){
    if(N-i*R<0){
      break;
    }
    for(int j=0;j<(int)3000/G+1;j++){
      if(N-i*R-j*G<0){
        break;
      }
      if((N-i*R-j*G)%B == 0){
        ans += 1;
      }
    }
  }
  cout<<ans<<endl;
  return 0;
}
