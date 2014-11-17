# 1353  - 3
 
dp = Array.new(10) {Array.new(82,0)}



1.upto(9).each {|i| dp[1][i] = 1}
2.upto(9).each {|i|
   1.upto(81).each {|j|
      dp[i][j] = dp[i-1][j]  # last make  0 
      k = 1 
      while (k <=9 ) and j >= k 
         dp[i][j] += dp[i-1][j-k]
         k += 1
      end
   }
}

n = gets.chomp!.to_i ;ans=0
if n==1
   puts 10
else
   1.upto(9).each {|i| ans += dp[i][n]}
   puts ans
end
   
