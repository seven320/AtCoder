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

int N,W;
int N_MAX = 100;
vector<int> w(N_MAX);
vector<int> v(N_MAX);


int rec(int i,int j){
  int res;
  if(i>=N){
    res = 0;
  }
  else if(j<w[i]){
    res = rec(i+1,j);
  }
  else{
    res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i]);
  }
  return res;
}

int main(){
  cin>>N>>W;
  for(int i=0;i<N;i++){
    cin>>v[i]>>w[i];
  }
  int ans = rec(0,W);
  cout<<ans<<endl;


  return 0;
}
