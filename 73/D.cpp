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
  int N,M,R;
  cin>>N>>M>>R;
  vector<int> r(R);

  for(int i=0;i<R;i++){
    cin>>r[i];
  }
  sort(r.begin(),r.end());
  int ways[M][3];
  for(int i=0;i<M;i++){
    cin>>ways[i][0]>>ways[i][1]>>ways[i][2];
  }
  // warshall_floyd
  int cost[N][N];
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cost[i][j]=INF;
    }
  }

  for(int i=0;i<M;i++){
    cost[ways[i][0]-1][ways[i][1]-1] = ways[i][2];
    cost[ways[i][1]-1][ways[i][0]-1] = ways[i][2];
  }

  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      for(int k=0;k<N;k++){
        cost[j][k] = min(cost[j][k],cost[j][i]+cost[i][k]);
      }
    }
  }

  ll ans = INF;
  int cnt = 0;
  do{
    ll tmp = 0;
    cnt += 1;
    for(int i=0;i<R-1;i++){
      tmp += cost[r[i]-1][r[i+1]-1];
    }
    ans = min(ans,tmp);
  }
  while( next_permutation(r.begin(),r.end()) );

  cout<<ans<<endl;
  // cout<<cnt<<endl;
  return 0;
}
