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
  int a,b,c,d;
  cin>>a>>b>>c>>d;
  int ans = 0;
  ans += min(a,b);
  ans += min(c,d);
  cout<<ans<<endl;
  return 0;
}
