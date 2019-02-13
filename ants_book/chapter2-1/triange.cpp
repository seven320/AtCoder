//encoding:utf-8

#include<iostream>
#include<string>

using namespace std;

//input
int n,a[MAX_N];

void solve(){
  int ans = 0;


  for (int i = 0; i<n; i++){
    for (int j = i; j<n; j++){
      for (int k = j; k<n; k++){
        int len = a[i]+a[j]+a[k];
        int ma = max(a[i], max(a[j],a[k]));
        if (ma < len-ma){
          ans = max(ans,len);
        }
      }
    }
  }
  //output
  printf("%d\n",ans);
}
