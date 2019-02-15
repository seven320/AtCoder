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


int solve(char T){
  int ans = 0;
  cout<<T<<endl;
  return ans;
}


int main(){
  int T;
  cin>>T;
  char S[T];
  for(int i=0;i<T;i++){
    cin>>S[i];
  }
  for(int i=0;i<T;i++){
  cout<<solve(S[i])<<endl;
  }
  return 0;
}
