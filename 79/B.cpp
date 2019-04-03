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
  int n;
  cin>>n;
  long long a,b;
  a = 2;
  b = 1;
  for(int i=0;i<n;i++){
    swap(a,b);
    b = a+b;
  }
  cout<<a<<endl;
  return 0;
}
