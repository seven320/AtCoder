//encoding:utf-8

#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
#define double long double

using namespace std;



int a[20];

bool dfs(int n,int k,int i,int sum){
  if(i==n) return sum==k;

  if(dfs(n,k,i+1,sum)) return true;

  if(dfs(n,k,i+1,sum+a[i])) return true;

  return false;
}


int main(){
  int n,k;
  scanf("%d",&n);

  for(int i=0;i<n;i++) scanf("%d",&a[i]);
  scanf("%d",&k);

  if(dfs(n,k,0,0)){
    printf("Yes\n");
  }
  else printf("No\n");
  return 0;
}
