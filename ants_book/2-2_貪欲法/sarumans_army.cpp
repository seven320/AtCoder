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
int main(){
  int n,r;
  cin>>n>>r;
  vector<int>x(n);
  for(int i=0;i<n;i++){
    cin>>x[i];
  }
  sort(x.begin(),x.end());
  int ans = 1;
  int position=x[0]+r;
  for(int i=1;i<n;i++){
    if(x[i]>=position+r){
      ans++;
      position = x[i]-r;
    }
  }
  cout<<ans<<endl;
  return 0;
}
