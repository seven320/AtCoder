//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<algorithm> //sort とかにいる

#define ll long long
using namespace std;

vector<char>s(3);

int main(){
  for(int i=0;i<3;i++){
    cin>>s[i];
  }
  sort(s.begin(),s.end());
  if(s[0]=='a' && s[1]=='b' && s[2]=='c'){
    cout<<"Yes"<<endl;
    return 0;
  }
  cout<<"No"<<endl;

  return 0;
}
