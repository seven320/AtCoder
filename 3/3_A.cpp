//encoding:utf-8

#include <iostream>
using namespace std;

int main(int argc,char** argv){
  int task;
  cin>>task;
  int answer;
  answer = task*(task+1)/2*10000/task;
  cout<<answer<<"\n";
  return 0;
}
