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

// int main(){
//   int a;
//   cin>>a;
//   cout<<a<<endl;
// }
int main(){
  int n,d,x;
  cin>>n>>d>>x;
  vector<int>a(n+1);
  for(int i=0;i<n;i++){
    cin>>a[i];
    // cout<<i<<endl;
  }

  int ans = x;
  int days;
  for(int i=0;i<n;i++){
    days = 1;
    while(days<=d){
      ans += 1;
      days += a[i];
    }
  }

  cout<<ans<<endl;
  return 0;
}
