## 1658  sum of digits  others

len = Array.new(Array.new)
dig = Array.new(Array.new)
num = Array.new



=begin
All the test cases given in this forum are working.But giving WA 1

my code is:
#include <stdio.h>
#include <string.h>
 int len[910][8110];
 int dig[910][8110];
 int num[110];

 int main(){
  int t,s1,s2,k,pt,i,j,l,temp;
  memset(len,0,sizeof(len));
  for(i=1;i<=900;i++){
      for(j=1;j<=8100;j++){
          for(k=1;k<=9;k++){
              if((i-k)<0||(j-k*k)<0)
                  break;
              else if((i-k)==0&&(j-k*k)==0){
                  len[i][j] = 1;
                  dig[i][j] = k;
              }
              else if(len[i-k][j-k*k]>0){
                  if(len[i-k][j-k*k]+1<len[i][j]||len[i][j]==0){
                      len[i][j] = len[i-k][j-k*k]+1;
                      dig[i][j] = k;
                  }
              }
              else
                  continue;
          }
      }
  }
  scanf("%d",&t);
  while(t--){
  scanf("%d %d",&s1,&s2);
  pt = 0;
  if(len[s1][s2]==0||len[s1][s2]>100)
      printf("No Solution");
  else{
        i=s1;
        j=s2;
      while((len[i][j]>=1)&&i>=1&&j>=1){
          l = dig[i][j];
          num[pt++] = l;
          i = i-l;
          l = l*l;
          j-=l;
      }
      for(i=0;i<pt;i++){
        for(j=i+1;j<pt;j++){
            if(num[i]>num[j]){
             temp=num[i];
             num[i]=num[j];
             num[j] = temp;
            }
        }
      }
      for(i=0;i<pt;i++)
          printf("%d",num[i]);
  }
  printf("\n");
  }
  return 0;
 }
Re: WA 1 esger 9 Apr 2013 13:40
Your mistake is here:

      if(len[i-k][j-k*k]+1<len[i][j]||len[i][j]==0){
          len[i][j] = len[i-k][j-k*k]+1;
          dig[i][j] = k;
          }
length might be the same but the value might be smaller. You just check the length.

=end