//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
using namespace std;

char s[3];
int ans;

int main(){
  cin>>s;
  ans = 700;
  for(int i=0;i<3;i++){
    if(s[i]=='o'){
      ans += 100;
    }
  }
  cout<<ans<<endl;

  return 0;
}
