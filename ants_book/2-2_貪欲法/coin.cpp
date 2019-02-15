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


int V[6]={1,5,10,50,100,500};

int C[6];
int X;
int ans=0;

int main(){
  cin>>X;
  // X = 1000-X;
  for(int i=5;i>=0;i--){
    C[i]=X/V[i];
    X -=V[i]*C[i];
    ans+=C[i];
  }
  cout<<ans<<endl;

  return 0;
}
