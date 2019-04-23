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
int N;
cin>>N;
vector<ll> a(N);
ll tmp;
for(int i=0;i<N;i++){
  cin>>a[i];
}
int cnt_4=0,cnt_2=0,cnt_0=0;
for(int i=0;i<N;i++){
  if(a[i]%4==0){
    cnt_4+=1;
  }
  else if(a[i]%2==0){
    cnt_2 += 1;
  }
  else{cnt_0+=1;
  }
}
string ans="No";
if(cnt_0==0){
  if(cnt_2 > 1 || cnt_4 > 0) ans = "Yes";
}
else{
  if (cnt_2 % 2 == 0 && cnt_4+1 >= cnt_0) ans="Yes";
  else if (cnt_2 % 2 == 1 && cnt_4 >= cnt_0) ans = "Yes";
}
cout<<ans<<endl;
  return 0;
}
