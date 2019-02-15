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
  int N;
  cin>>N;
  char S[N],T[N];
  for(int i=0;i<N;i++){
    cin>>S[i];
  }
  int a=0,b=N-1;
  while(a<=b){
    bool left=false;
    for(int i=0;a+i<=b;i++){
      if(S[a+i]>S[b-i]){
        break;
      }
      else if(S[a+i]<S[b-i]){
        left=true;
        break;
      }
      // S[a+i]==S[b-i]の場合i++によりさらに内側を参照している
    }
    if(left){
      putchar(S[a]);
      a++;
    }
    else{
      putchar(S[b]);
      b--;
    }
  }
  return 0;
}
