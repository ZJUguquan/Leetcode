# 1119 metro
# finals before? 
n,m =gets.chomp!.split(" ").map(&:to_i)
k = gets.chomp!.to_i 
$path =[]  
1.upto(k).each {|e|   $path << gets.chomp!.split(" ").map(&:to_i)}
#p $path
def min(x,y) ;   return x > y ? y : x     end

def shortest(n,m)
   if n == 0  
      return m * 100
   elsif m == 0
      return n * 100
   else
      if $path.include?([n,m])
         return [shortest(n-1,m-1)+ Math.sqrt(2) * 100, shortest(n-1,m)+100,shortest(n,m-1) + 100].min
         #[shortest(n-1,m-1)+ Math.sqrt(2) * 100, min(shortest(n-1,m),shortest(n,m-1)) + 100)
      else
         return  min(shortest(n-1,m), shortest(n,m-1)) + 100
         #min(,) + 100
      end
   end
end
puts shortest(n,m).round
    
    
=begin
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MAX = 1005;
const double d = 100*sqrt(2.0);
double dp[2][MAX];
bool map[MAX][MAX];
int ex,ey;
int main()
{
	int k,x,y;
	memset(map,false,sizeof(map));
	scanf("%d %d",&ex,&ey);
	ex++; ey++;
	scanf("%d",&k);
	while( k-- )
	{
		scanf("%d %d",&x,&y);
		map[x][y] = true;
	}
	memset(dp,0,sizeof(dp));
	for(int i=2; i<=max(ex,ey); i++)
		dp[0][i] = i*100 - 100;
	for(int i=2; i<=ex; i++)
	{
		dp[1][1] = i*100 - 100;
		for(int k=2; k<=ey; k++)
			if( map[i-1][k-1] )
				dp[1][k] = min( min( dp[0][k-1] + d, dp[1][k-1]+100.0 ), dp[0][k] + 100 );
			else
				dp[1][k] = min( dp[0][k], dp[1][k-1]) + 100;
		memcpy(dp[0],dp[1],sizeof(dp[1]));
	}
	printf("%.0lf/n",dp[0][ey]);
return 0;
}

=end