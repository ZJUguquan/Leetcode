# acm 1106  where my friends
# two teams


#read data
#n = gets.chomp.to_i

a = Array.new(Array.new)
p a.class


=begin
  
I used BFS.
#include<stdio.h>
#define maxn 1200
int a[maxn][maxn], queue[maxn], n, d, c, ans[maxn], k;
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<n;j++){
            scanf("%d",&a[i][j]);
            if(a[i][j]>0) a[i][0]++;
            else break;
        }
    }
    if(n<=1){
             printf("0");
             return 0;
       }
    for(int i=1;i<=n;i++)
       if(a[i][0]==0){
             printf("0");
             return 0;
       }
    d = 1;
    for(int i=1;i<=n;i++){
        if(ans[i]==0){
           ans[i] = 1;
           k++;
           c++;
           queue[c] = i;
           do{
              for(int i=1;i<=a[queue[d]][0];i++){
                 if(ans[a[queue[d]][i]]==0){
                     ans[a[queue[d]][i]]=ans[queue[d]]+1;
                     if(ans[a[queue[d]][i]]%2) k++;
                     c++;
                     queue[c] = a[queue[d]][i];
                 }
              }
              d++;
           }while(d<=c);
        }
    }
    printf("%d\n",k);
    for(int i=1;i<=n;i++)
       if(ans[i]%2) printf("%d ",i);
    return 0;
}
Help me! please!
end