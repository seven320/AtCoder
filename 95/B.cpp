//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<algorithm>

#define ll long long
using namespace std;


// int n,x;
// int m[100];
// int donut;
// int min_value = pow(10,5);
//
// int main(){
//   donut = 0;
//   cin>>n>>x;
//
//   for(int i=0;i<n;i++){
//     cin>>m[i];
//     x-=m[i];
//     donut++;
//     if(min_value>m[i]){
//       min_value = m[i];
//     }
//   }
//   donut+=x/min_value;
//   cout<<donut<<endl;
//   return 0;
// }

int main(){
  int n,x;
  cin>>n>>x;
  int count=0;
  vector<int> m(n);
  for(int i=0;i<n;i++){
    cin>>m[i];
    x-=m[i];
  }
  sort(m.begin(),m.end());
  cout<<n+x/m[0]<<endl;
  return 0;
}
