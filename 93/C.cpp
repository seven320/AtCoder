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
  vector<int>nums(3);
  int even=0;
  int ans=0;
  for(int i=0;i<3;i++){
    cin>>nums[i];
    if(nums[i]%2==0){
      even++;
    }
  }
  if(even==3){
  }
  else if(even==2){
    for(int i=0;i<3;i++){
      if(nums[i]%2==0){
        nums[i]+=1;
      }
    }
  ans++;
  }
  else if(even==1){
    for(int i=0;i<3;i++){
      if(nums[i]%2==1){
        nums[i]+=1;
      }
    }
  ans++;
  }
  else{}
  int max = 0;
  int sum = 0;
  for(int i=0;i<3;i++){
    sum += nums[i];
    if(max<nums[i]){
      max=nums[i];
    }

  }
  ans+=((3*max-sum)/2);

  cout<<ans<<endl;
  return 0;
}
