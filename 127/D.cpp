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
  int n,m;
  cin>>n>>m;
  vector<int> a(n);
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  vector<int> b(n),c(n);
  for(int i=0;i<m;i++){
    cin>>b[i]>>c[i];
  }

  sort(a.begin(),a.end());
  


  return 0;
}
