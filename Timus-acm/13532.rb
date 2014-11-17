# 1353 - 2
=begin
/*题意：求【1 to 10^9】范围内各位数字之和为s的数的个数；
　　思路：定义dp[i][j] (i = 1 to 9, j = 1 to 81)，表示位数为i的数各位数之和为j的数的个
数。dp[i][j] = (i - 1位数最低位全部补0) + (i - 1位数最高位补j - k {k| 1 <= k <= 9} )。所以转
移方程就是
　　dp[i][j] = dp[i-1][j] + sum(dp[i-1][j - 1] , dp[i-1][j-2] ,  ...  , dp[i-1][j-9]);

ps:注意s = 1 的时候是10而不是9，因为10^9也算在s = 1里边
=end
n = gets.chomp!.to_i ; ans= Array.new(100,0); temp = ans; 
if n == 1
   puts 10 
else
   0.upto(9).each {|i| ans[i] = 1}
   1.upto(8).each {|i| 
      0.upto(81).each {|k| 
         temp[k] = ans[k]
      }
      0.upto(9).each {|j|
         if j != 0 
            0.upto(81).each {|k|  ans[k] = temp [k] }
         end
      }
   }
end