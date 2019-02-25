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
  int n;
  cin>>n;
  int A[2][n];
  int B[2][n];
  for(int i=0;i<2;i++){
    for(int j=0;j<n;j++){
      cin>>A[i][j];
      B[i][j] = 0;
    }
  }
  B[0][0] = A[0][0];
  B[1][0] = A[1][0]+A[0][0];

  for(int i=0;i<2;i++){
    for(int j=1;j<n;j++){
      if(i==0){
        B[i][j] = B[i][j-1]+A[i][j];
      }
      else{
        B[i][j] = max(B[i-1][j],B[i][j-1])+A[i][j];
      }

    }
  }
  cout<<B[1][n-1]<<endl;
  return 0;
}
