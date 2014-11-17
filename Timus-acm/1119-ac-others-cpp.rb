#=begin

#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<map>
#include<queue>
#include<algorithm>
#include<string.h>
#include<stack>
using namespace std;
struct node
{
    int x,y;
}mem[101];
bool cmp(node a,node b)
{
    if(a.x==b.x)
    return a.y<b.y;
    return a.x<b.x;
}
int main()
{
   //freopen("d:\\6\\bin\\Debug\\hu.txt","r",stdin);
   const double T=sqrt(2.0)*100;
   int a[101];
   int n,m,k,i,j,l,max;
   cin>>n>>m;
   cin>>k;
   for(i=0;i<k;i++)
   cin>>mem[i].x>>mem[i].y;
   if(k==0)
   {
       printf("%d\n",(n+m)*100);
       return 0;
   }
   sort(mem,mem+k,cmp);
   a[0]=1;l=1;
   for(i=1;i<k;i++)
   {
       max=0;
       for(j=0;j<i;j++)
       {
           if(mem[j].y<mem[i].y&&mem[j].x<mem[i].x&&a[j]>max)
           {
               max=a[j];
           }
           a[i]=max+1;
           if(a[i]>l)
           l=a[i];
       }
   }
   printf("%d\n",int((n+m)*100.0-l*(200.0-T)+0.5));
   return 0;
}

=end