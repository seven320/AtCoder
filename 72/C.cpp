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
  int a[N];
  int a_max = 0;
  for(int i=0;i<N;i++){
    cin>>a[i];
    if(a_max<a[i]){
      a_max = a[i];
    }
  }
  sort(a.begin(),a.end());
  for(int x=0;x<a_max;x++){
    int tmp = 0;
    for(int i=0;i<N;i++){
      tmp += abs(a[i]-a_max);
    }
    if(tmp>N){
      break;
    }
  }
  
  return 0;
}
