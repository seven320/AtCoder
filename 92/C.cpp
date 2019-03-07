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
  vector<int>a(n);
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  int all_path = 0;
  int position = 0;
  for(int i=0;i<n;i++){
    all_path += abs(position-a[i]);
    position = a[i];
  }
  all_path += abs(position);

  for(int i=0;i<n;i++){
    int ans = all_path;
    int pre_position,after_position;
    if(i==0){
      pre_position = 0;
    }
    else{
      pre_position = a[i-1];
    }
    if(i==n-1){
      after_position = 0;
    }
    else{
      after_position = a[i+1];
    }
    // cout<<pre_position<<a[i]<<after_position<<endl;
    if((pre_position<=a[i]&&a[i]<=after_position)||(pre_position>=a[i]&&a[i]>=after_position)){
    }
    else{
      ans -= abs(a[i]-pre_position)+abs(after_position-a[i]);
      ans += abs(pre_position-after_position);
    }
    cout<<ans<<endl;
  }
  return 0;
}
