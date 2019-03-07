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
int inf = INFINITY;

int main(){
  int n,k;
  cin>>n>>k;
  vector<int> h(n);
  for(int i=0;i<n;i++){
    cin>>h[i];
  }

  int ans = inf;
  sort(h.begin(),h.end());

  for(int i=0;i<n-k+1;i++){
    ans = min(h[i+k-1]-h[i],ans);
  }
  cout<<ans<<endl;
  return 0;
}
