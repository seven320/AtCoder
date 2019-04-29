//encoding:utf-8
//#include <iostream> //c++
//#include<stack> //スタックに関して　最新のデータから捨てる
//#include<queue> //キューに関して　最古のデータから捨てる
//#include<math.h>
//#include<vector>
//#include<algorithm> //sort とかにいる
#include<bits/stdc++.h>//vector,algorithm,que
#include<time.h> //時間にかんして

#define ll long long
#define MOD 1000000007
#define INF (1<<29)
using namespace std;

ll gcd( ll m, ll n ){
  if ( ( 0 == m ) || ( 0 == n ) )
  return 0;

	// ユークリッドの方法
  while( m != n ){
    if ( m > n ) m = m - n;
    else         n = n - m;
	}
  return m;
}


int main(){
  int N;
  cin>>N;
  vector<ll> A(N);
  for(int i=0;i<N;i++){
    cin>>A[i];
  }
  for(int i=0;i<N;i++){
    gcd()
  }


  return 0;
}
