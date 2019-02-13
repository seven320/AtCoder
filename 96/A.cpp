//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
using namespace std;

int month,day;
int ans=0;

int main(){
  cin>>month>>day;
  for(int i=1;i<=month;i++){
    if(day<=12){
      ans = month-1;
    }
    if(day>=month){
      ans++;
    }
  }
  cout<<ans<<"\n";
  return 0;
}
