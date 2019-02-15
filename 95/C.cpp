//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>

#define ll long long
using namespace std;
int a,b,c,x,y;
int count_c;
int price;

int main(){
  cin>>a>>b>>c>>x>>y;
  price = a*x+b*y;

  // if(a+b-2*c>0){
  //   price = max(x,y)*2*c;
  // }
  for(int i=0;i<=max(x,y)*2;i+=2){
    // cout<<i<<endl;
    price=min(max((x-i/2),0)*a+max((y-i/2),0)*b+i*c,price);
  }
  cout<<price<<endl;
  return 0;
}
