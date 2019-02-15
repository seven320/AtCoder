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
  int a,b,k;
  cin>>a>>b>>k;
  for(int i=a;i<=b;i++){
    if(i<a+k||b-k<i){
      cout<<i<<endl;
    }
  }
  return 0;
}
