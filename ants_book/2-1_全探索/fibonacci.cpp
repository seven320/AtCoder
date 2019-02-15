//encoding:utf-8

#include <iostream>
#include<time.h> //時間にかんして

#define ll long long
#define int long long
#define double long double

using namespace std;

// 再帰

long long fib(int n){
  if(n<=1){
    return n;
  }
  return fib(n-1)+fib(n-2);
}

// 再帰リストあり

long long memo[61];

long long fib_memo(int n){
  if(n<=1){
    return n;
  }
  if(memo[n]!=0){
    return memo[n];
  }
  return memo[n] = fib_memo(n-1)+fib_memo(n-2);
}



int main(){
  int n;
  cin>>n;
  clock_t start_time = clock();
  cout<<fib(n)<<"\n";
  clock_t end_time = clock();
  cout<<"elapsed time="<<(double)(end_time-start_time)/CLOCKS_PER_SEC<<"sec.\n";

  start_time = clock();
  cout<<fib_memo(n)<<"\n";
  end_time = clock();
  cout<<"elapsed time="<<(double)(end_time-start_time)/CLOCKS_PER_SEC<<"sec.\n";

  return 0;
}
