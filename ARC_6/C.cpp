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
  vector<int>w(n);
  vector<int>tower(n);
  // int w[n];
  // int tower[n];
  for(int i=0;i<n;i++){
    tower[i] = 0;
  }
  int ans=0;
  bool changed = false;
  for(int i=0;i<n;i++){
    cin>>w[i];
  }
  for(int i=0;i<n;i++){
    std::sort(tower.begin(),tower.begin()+ans);
    for(int j=0;j<n;j++){
      cout<<tower[j]<<" ";
    }
    cout<<endl;
    changed = false;
    for(int j=0;j<ans;j++){
      if(tower[j]>=w[i]){
        tower[j] = w[i];
        changed = true;
        break;
      }
    }
    if(!changed){
      tower[ans] = w[i];
      ans++;
    }

    // for(int k=0;k<ans;k++){
    //   cout<<tower[k]<<endl;
    // }


  }
  cout<<ans<<endl;
  return 0;
}
