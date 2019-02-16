//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる

#define ll long long
using namespace std;

int n,m;
int N_MAX=30,M_MAX=30;
int k;
int a[31][31]={0};
int memo[31]={0};


int main(){
  cin>>n>>m;
  // memset(a,0,sizeof(a));
  // memset(memo,0,sizeof(memo));
  for(int i=0;i<n;i++){
    cin>>k;
    for(int j=0;j<k;j++){
      cin>>a[i][j];
    }
  }
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(a[i][j]!=0){
        memo[a[i][j]]++;
      }
    }
  }
  int ans=0;
  for(int i=0;i<31;i++){
    if(memo[i]==n){
      ans++;
    }
  }
  cout<<ans<<endl;
  return 0;
}
