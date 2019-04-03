//encoding:utf-8
#include<time.h> //時間にかんして
// #include<stack> //スタックに関して　最新のデータから捨てる
// #include<queue> //キューに関して　最古のデータから捨てる
// #include<math.h>
// #include<vector>
// #include<algorithm> //sort とかにいる
#include<bits/stdc++.h>//vector,algorithm,que
#define int long long //int　宣言をlong longとする


using namespace std;
signed main(){
  int N;
  cin>>N;
  int A[N],B[N],C[N];//これはリスト
  //v()を使いたいなvector

  for(int i=0;i<N;i++){
    cin>>A[i];
  }
  for(int i=0;i<N;i++){
    cin>>B[i];
  }
  for(int i=0;i<N;i++){
    cin>>C[i];
  }

  sort(A,A+N);
  sort(B,B+N);
  sort(C,C+N);

  int sum = 0;
  for(int i=0;i<N;i++){
    auto itr1 = lower_bound(A,A+N,B[i]);
    int a = itr1-A;
    // cout<<a<<endl;

    auto itr2 = upper_bound(C,C+N,B[i]);
    int c = C+N-itr2;
    // cout<<c<<endl;
    sum = sum + c*a;
  }
  cout<<sum<<endl;


  return 0;
}
