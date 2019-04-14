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
using namespace std;
int main(){
  int N,K;
  cin>>N>>K;
  string S;
  cin>>S;

  vector<int> Nums;
  int now = 1;//今みている数
  //もし最初の数字が0ならその分がカウントされる
  int cnt = 0;
  for(int i=0;i<N;i++){
    if(S[i]==(char)('0'+now))cnt++;
    else{
      Nums.push_back(cnt);
      now = 1 - now;
      cnt = 1;
    }
  }

  if(cnt!=0) Nums.push_back(cnt);

  if(Nums.size()%2==0)Nums.push_back(0);

  int Add = 2 * K + 1;
  int ans = 0;
  //1-0-...の1から始めるの
  for(int i=0;i<Nums.size();i+=2){
    int tmp = 0;
    int left = i;
    int right = min(i+Add,(int)Nums.size());
    for(int j=left;j<right;j++){
      tmp += Nums[j];
    }
    ans = max(ans,tmp);
  }

  cout<<ans<<endl;
  return 0;
}
