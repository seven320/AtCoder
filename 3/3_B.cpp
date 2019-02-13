//encoding:utf-8

#include <iostream>
#include<string>
#include<functional>
using namespace std;

int main(int argc,char** argv){
  string s,t;
  cin>>s>>t;
  bool ans=true;

  for(int i;i<s.size();i++){
    if(s[i]==t[i]) continue;
    if(t[i]=='@') swap(s[i],t[i]);
    if(s[i]=='@'&&string("atcoder").find(t[i]) != string::npos)continue;
    else{
      ans=false;
    }
  }
  if(ans){
    cout<<"You can win"<<"\n";
  }
  else{
    cout<<"You will lose"<<"\n";
  }
  return 0;
}
