//encoding:utf-8

#include <iostream>
#include<time.h> //時間にかんして
#include<stack>

#define ll long long
#define double long double

using namespace std;

int main(){
  stack<int> s;
  s.push(1);    //{}>{1}
  s.push(2);    //{1}>{1,2}
  printf("%d\n",s.top());
  s.pop();    //{1,2}>{1}
  printf("%d\n",s.top());
  return 0;
}
