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
using namespace std;
int main(){
  int A,B,C,D,E,F;
  cin>>A>>B>>C>>D>>E>>F;
  vector<int> water;
  for(int a=1;a<(int)F/(A*100);a++){
    for(int b=0;b<(int)F/(B*100);b++){
      water.push_back((a*A+b*B)*100);
    }
  }



  vector<int> suger;
  for(int c=0;c<(int)F/C;c++){
    for(int d=0;d<(int)(F-c)/D;d++){
      suger.push_back(c*C+d*D);
    }
  }

  long pure = 0;
  int ans_w=0,ans_s=0;
  for(int wi=0;wi<water.size();wi++){
    for(int si=0;si<suger.size();si++){
      if(water[wi]+suger[si]>F)break;
      else{
        cout<<"hoge"<<(suger[si]/(water[wi]+suger[si]))<<endl;
        if(pure<(suger[si]/(water[wi]+suger[si]))<(E/(100+E))){
          ans_w = water[wi];
          ans_s = suger[si];
          pure = suger[si]/(water[wi]+suger[si]);
        }
      }
    }
  }

  cout<<ans_w<<ans_s<<endl;
  return 0;
}
