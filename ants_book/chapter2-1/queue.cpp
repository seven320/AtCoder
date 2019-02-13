//encoding:utf-8

#include <iostream>
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる

#define ll long long
#define double long double

using namespace std;

int main(){
  queue<int> que;
  que.push(1);
  que.push(2);
  que.push(3);
  printf("%d\n",que.front());
  que.pop();
  printf("%d\n",que.front());
}
