//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
using namespace std;

int h,w;
int MAX_H=50,MAX_W=50;
char s[50][51];
// int visited[MAX_H][MAX_W];

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int visit(int x,int y){
  for(int i=0;i<4;i++){
    int nx=x+dx[i],ny=y+dy[i];
    if(0<=nx<h && 0<=ny<w && s[nx][ny]=='#'){
      return true;
    }
  }
  return false;
}

int main(){
  cin>>h>>w;
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      cin>>s[i][j];
      // visited[i][j]=0;
    }
  }
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if(s[i][j]=='#'){
        if(!visit(i,j)){
          cout<<"No"<<endl;
          return 0;
        }
      }
    }
  }
  cout<<"Yes"<<endl;
  return 0;
}
