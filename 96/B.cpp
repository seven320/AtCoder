//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>

#define ll long long
using namespace std;

int a,b,c,k;
int ans = 0;

int main(){
  cin>>a>>b>>c>>k;
  if(max(a,max(b,c))==a){
    ans = pow(2,k)*a+b+c;
  }
  else if(max(a,max(b,c))==b){
    ans = pow(2,k)*b+a+c;
  }
  else{
    ans= pow(2,k)*c+a+b;
  }
  cout<<ans<<endl;
  return 0;
}
