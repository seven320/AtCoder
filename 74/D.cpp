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
  int N;
  cin>>N;
  ll A[N][N];
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cin>>A[i][j];
    }
  }
  ll ans = 0;
  bool exist = true;
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      for(int k=0;k<N;k++){
        if(A[j][k] > A[j][i]+A[i][k]){
          exist = false;
        }
      }
    }
  }
  if(exist){
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++){
        ll tmp = 100000000000;
        for(int k=0;k<N;k++){
          if(i==k||j==k){
          }
          else if(tmp>A[i][k]+A[k][j]){
            tmp = A[i][k]+A[k][j];
          }
        }
        if(A[i][j] < tmp){
          ans += A[i][j];
        }
      }
    }
    ans = ans/2;
  }
  if(exist){
  }
  else{
    ans = -1;
  }
  cout<<ans<<endl;

  return 0;
}
