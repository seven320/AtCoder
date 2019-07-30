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


int H,W;
int cnt;
char S[2001][2001];
ll lights[2001][2001][2];

int count_ver(int i,int j){
  int cnt = 0;
  for(int x=i;x<W;x++){
    if (S[j][x] == '.') {
      cnt ++;
    }
    else{
      break;
    }
  }
  for(int x=i;x<W;x++){
    if (S[j][x] == '.') {
      lights[j][x][0] = cnt;
    }
    else{
      break;
    }
  }
  return cnt;
}


int count_hor(int i,int j){
  cnt = 0;
  for(int y=j;y<H;y++){
    if (S[y][i] == '.') {
      cnt ++;
    }
    else{
      break;
    }
  }
  for(int y=j;y<H;y++){
    if (S[y][i] == '.') {
      lights[y][i][1] = cnt;
    }
    else{
      break;
    }
  }
  return cnt;
}

int main(){
  cin>>H>>W;
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      cin>>S[i][j];
    }
  }

  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      for(int k=0;k<2;k++){
        lights[i][j][k] = 0;
      }
    }
  }
  int ans = -1;
  int ver = 0,hor =0 ;
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      // cout<<S[i][j]<<endl;
      if(S[i][j] == '.'){
        ver = lights[i][j][0];
        hor = lights[i][j][1];
        if(ver==0){
          ver = count_ver(j,i);
        }
        if(hor==0){
          hor = count_hor(j,i);
        }
        ans = max(ans,hor+ver-1);
        // cout<<ans<<endl;
      }
    }
  }
  cout<<ans<<endl;
  return 0;
}
