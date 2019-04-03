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
  string n;
  cin>>n;
  bool ans;
  if((n[0]==n[1]&&n[1]==n[2])||(n[1]==n[2]&&n[2]==n[3])){
    ans = true;
  }
  else{
    ans = false;
  }
  if(ans){
    cout<<"Yes"<<endl;
  }
  else{
    cout<<"No"<<endl;
  }
  return 0;
}
