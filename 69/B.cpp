//encoding:utf-8
//#include <iostream> //c++
//#include<stack> //スタックに関して　最新のデータから捨てる
//#include<queue> //キューに関して　最古のデータから捨てる
//#include<math.h>
//#include<vector>
//#include<algorithm> //sort とかにいる
#include<bits/stdc++.h>//vector,algorithm,que
#include<time.h> //時間にかんして

#define ll long long
#define MOD 1000000007
#define INF (1<<29)
using namespace std;
int main(){
  string s;
  cin>>s;
  string ans[2];
  int cnt = 0;
  for(int i=0;i<s.length();i++){
    if(i==0){
      ans[0] = s[0];
    }
    else if(i==s.size()-1){
      ans[1] = s[i];
    }
    else{
      cnt +=1;
    }
  }
  // ans[1] = cnt;
  cout<<ans[0]<<cnt<<ans[1]<<endl;
  return 0;

  
}
