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

const int MAX_N=10000;

int S[MAX_N],T[MAX_N];


int main(){
  int n;
  cin>>n;
  int s[n];
  int t[n];
  for(int i=0;i<n;i++){
    cin>>s[i];
  }
  for(int i=0;i<n;i++){
    cin>>t[i];
  }
  pair<int,int>itv[MAX_N];
  for(int i=0;i<n;i++){
    itv[i].first = t[i];
    itv[i].second = s[i];
  }
  sort(itv,itv+n);
  int ans=0,now=-1;
  for(int i=0;i<n;i++){
    if(now<itv[i].second){
      ans++;
      now = itv[i].first;
    }
  }
  cout<<ans<<endl;
  return 0;
}
