#include<iostream> //input
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<map>
#include<iomanip>
#include<queue>
#include<stack>
#include<time.h>
#define rep(i,n)for(ll i=0;i<n;i++)
#define ll long long
using namespace std;

// signed main(){
//   char name[10];
//   cout<<"お名前は？　　";
//   cin>>name;
//   cout<<endl;
//   cout<<"こんにちは　　"<<name<<"さん";
// }

int list[10];

int main(){
  for(int i=0;i<10;i++){
    list[i] = i;
  }
  cout<<list[0]<<list[1];
  return 0;
}
