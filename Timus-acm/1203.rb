# 1203 Scientific Conference 

n = gets.chomp!.to_i     ;  dp = Array.new(30001,0)
if n == 0
   puts 0
elsif n == 1
   puts 1
else # n > 1
   
  1.upto(n).each {|i|
     s, e = gets.chomp!.split(" ").map(&:to_i)
     if dp[e] < s then dp[e] = s end
        
  }
  
  1.upto(30000).each {|i| 
     if dp[i] > 0
        if dp[dp[i] -1] +1 > dp[i-1]  
            dp[i] = dp[dp[i]-1] + 1 
         else
            dp[i] = dp[i-1]
         end
      else
         dp[i] = dp[i-1]
      end
  }
  puts dp[30000]
   # a = input.split("\n")
   # a.each 
   
end