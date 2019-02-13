//encoding:utf-8

#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long

using namespace std;

// global
int n,m;
char field[100][101];


void change2land(int x,int y){
  field[x][y]='.';
  for(int dx=-1;dx<2;dx++){
    for(int dy=-1;dy<2;dy++){
      int nx=x+dx;
      int ny=y+dy;
      if(0<=nx<n && 0<=ny<m && field[nx][ny]=='W'){
        change2land(nx,ny);
      }
    }
  }
}

void solve(){
  int count=0;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(field[i][j]=='W'){
        change2land(i,j);
        count++;
      }
    }
  }
  cout<<count<<"\n";
}

int main(){
  cin>>n>>m;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      cin>>field[i][j];
    }
  }
  solve();
}
