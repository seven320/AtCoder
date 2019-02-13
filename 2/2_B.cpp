//encoding:utf-8

#include <iostream>
using namespace std;

int main(int argc,char** argv){
  string w;
  cin>>w;
  for (int i=0; i<w.length();i++){
    if(w[i]=='a'||w[i]=='i'||w[i]=='o'||w[i]=='u'||w[i]=='e'){
      w.erase(w.begin()+i);
      i -= 1;
    }
  }
  cout << w<<"\n";
  return 0;
}
