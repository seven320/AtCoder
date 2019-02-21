//encoding:utf-8
// Longet Common Subsequencs
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる

#define ll long long
using namespace std;
int main(){
  int n,m;
  cin>>n>>m;
  char s[n],t[m];
  for(int i=0;i<n;i++){
    cin>>s[i];
  }
  for(int i=0;i<m;i++){
    cin>>t[i];
  }
  int dp[n+1][m+1];
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      dp[i][j]=0;
    }
  }

  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(s[i]==t[j]){
        dp[i+1][j+1]=dp[i][j]+1;
      }
      else{
        dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1]);
      }
    }
  }
  // for(int i=0;i<n;i++){
  //   cout<<dp[i][i];
  // }
  cout<<dp[n][m]<<endl;
  return 0;
}
