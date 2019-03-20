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
int inf = INFINITY;
int main(){
  int n;
  cin>>n;
   std::vector<std::vector<int>> datas{{1, 2, 3}, {4, 5, 6}};
  for(int i=0;i<n;i++){
    for(int j=0;j<3;j++){
      cin>>datas[i][j];
    }
  }

  return 0;
}
