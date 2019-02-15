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
  int n;
  cin>>n;
  vector<int> l(n);
  for(int i=0;i<n;i++){
    cin>>l[i];
  }
  ll ans=0;
  sort(l.begin(),l.end());
  while(n>1){
    int mil1=0,mil2=1;
    for(int i=2;i<n;i++){
      if(l[i]<l[mil1]){
        mil2=mil1;
        mil1 = i;
      }
      else if(l[i]<l[mil2]){
        mil2=i;
      }
    }

  int t = l[mil1]+l[mil2];
  ans += t;
  cout<<ans<<endl;

  if(mil1==n-1)swap(mil1,mil2);
  l[mil1]=t;
  l[mil2]=l[n-1];
  n--;
  }
  cout<<ans<<endl;
  return 0;
}
