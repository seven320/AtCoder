//encoding:utf-8
#include <iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる

#define ll long long
using namespace std;


int main(){
  vector<int> v(5);
  for(int i=0;i<v.size();i++){
    v[i]=5-i;
  }
  //通常のソート
  sort(v.begin(),v.end()); //{1,2,3,4,5}
  for(int i=0;i<v.size();i++){
    cout<<v[i];
  }
  cout<<endl;
  for(int i=0;i<v.size();i++){
    v[i]=5-i;
  }

//一部分のソート
  sort(v.begin(),v.begin()+1);//{5,4,3,2,1}
  for(int i=0;i<v.size();i++){
    cout<<v[i];
  }
  cout<<endl;
  for(int i=0;i<v.size();i++){
    v[i]=5-i;
  }

  sort(v.begin(),v.begin()+3);//{4,5,3,2,1}
  for(int i=0;i<v.size();i++){
    cout<<v[i];
  }
  return 0;
}

// #include <iostream>
//
// //C++14
// auto f(){
//   return 14;// 関数f()の定義で、戻り値の型は int となる。
// }
//
// int main(){
//
//   // C++11
//   auto num = 11;
//   auto name = "hoge";
//
//   std::cout << num << name <<std::endl;
//
//   //C++14
//   int x = f();
//   std::cout << x<<std::endl;
// }
