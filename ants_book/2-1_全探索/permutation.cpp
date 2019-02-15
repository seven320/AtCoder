//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
using namespace std;

// int MAX_N = 100000;
const int MAX_N = 10000;
bool used[MAX_N];
int perm[MAX_N];

//{0,1,2,3,...n-1}の並び替えn!通りを生成する

void permutation1(int pos,int n){
  if(pos==n){
    return ;
  }
  //perm　のpos 番目を0~n-1にするかのループ
  for(int i=0;i<n;i++){
    if(!used[i]){
      perm[pos] = i;
      used[i] = true;
      permutation1(pos+1,n);
      //戻ってきたらフラグ戻す
      used[i]=false;
    }
  }
  return ;

}

// #include<algorithm>
//
// int perm2[MAX_N];
//
// void permutation2(int n){
//   for(int i=0;i<n;i++){
//   perm2[i] = i;
//   }
//   do{
//
//   }while(next_permutation(perm2,perm2+n));
//   return ;
// }

int main(){
  for(int i=0;i<10;i++){
      perm[i] = i;
  }


  permutation1(0,1);
  for(int i=0;i<10;i++){
    cout<<perm[i];
  }
  return 0;
}
