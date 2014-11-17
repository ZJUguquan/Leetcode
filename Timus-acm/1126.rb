# 1126  Magnetic Storms


#include<iostream>
#include<queue>
#include<vector>
using namespace std;
int izv[100001];
int main(){
int m;
cin>>m;
priority_queue<int>k;
vector<int>x;
int a,br=0;
while(1)
{
cin>>a;
if(a==-1)break;
x.push_back(a);
k.push(a);
br++;
if(br==m)cout<<k.top()<<endl;
else
if(br>m)
{
izv[x[0]]++;
x.erase(x.begin());
while(izv[k.top()]){izv[k.top()]--;k.pop();}
cout<<k.top()<<endl;
}
}

system("pause");
return 0;
}


