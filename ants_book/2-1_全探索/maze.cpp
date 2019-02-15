//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
using namespace std;

const int INF = 10000;

typedef pair<int,int> P;

int n,m;
char field[100][101];
int sx,sy;
int gx,gy;
//最短郷里を保存
int d[100][100];

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

int bfs(){
  queue<P> que;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      d[i][j] = INF;
    }
  }
  que.push(P(sx,sy));
  d[sx][sy] = 0;

  //que が空になるまでループ
  while(que.size()){
    P p = que.front();
    que.pop();

    if(p.first==gx && p.second==gy){
      break;
    }
    for(int i=0;i<4;i++){
      int nx = p.first+dx[i];
      int ny = p.second+dy[i];

      if (0<=nx && nx<n && 0<=ny && ny<m && field[nx][ny]!='#' && d[nx][ny]==INF){
        que.push(P(nx,ny));
        d[nx][ny] = d[p.first][p.second]+1;
      }
    }
  }
  return d[gx][gy];
}

int main(){
  cin>>n>>m;
  cin>>sx>>sy>>gx>>gy;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){

      cin>>field[i][j];
    }

  }
  sy--;
  sx--;
  gx--;
  gy--;
  int ans = bfs();
  cout<<ans<<"\n";
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      cout<<d[i][j]<<" ";
    }
    cout<<"\n";
  }
  return 0;
}
