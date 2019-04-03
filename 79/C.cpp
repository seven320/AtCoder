//encoding:utf-8
#include<iostream> //c++
#include<time.h> //時間にかんして
#include<stack> //スタックに関して　最新のデータから捨てる
#include<queue> //キューに関して　最古のデータから捨てる
#include<math.h>
#include<vector>
#include<algorithm> //sort とかにいる
// #include<bits/stdc++.h>


// #include<bits/stdc++.h>
#define ll long long

using namespace std;
int inf = INFINITY;
int main(){
  int n;
  cin>>n;
  int A[n],B[n],C[n];

  for(int i=0;i<n;i++){
    cin>>A[i];
  }
  for(int i=0;i<n;i++){
    cin>>B[i];
  }
  for(int i=0;i<n;i++){
    cin>>C[i];
  }

  sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  sort(C.begin(),C.end());

  int sum = 0;
  for(int i=0;i<n;i++){
    auto itr1 = lower_bound(A.begin(),A.end(),B[i]);
    int a = itr1-A.begin()
    cout<<a<<endl;

    auto itr2 = upper_bound(C.begin(),C.end(),B[i]);
    int c = C.end()-itr2;
    cout<<c<<endl;

    sum += a*c;
  }
  cout<<sum<<endl;


  return 0;
}
