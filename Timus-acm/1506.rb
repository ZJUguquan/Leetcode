# 1506  columns of numbers

n, k =[11,3]     ;arr = [1,2,3,4,5,6,7,8,9,10,11]     
n,k=gets.chomp!.split(" ").map(&:to_i)
arr= gets.chomp!.split(" ").map(&:to_i)

k = (n+k-1) / k ; 
0.upto(k-1).each {|i|
   j = i 
   while (j<n)
      printf "%4d",arr[j]
      j += k
   end
   puts 
}
# 
# dp = Array.new(n/k+1) {Array.new(k,0)}
# 0.upto(n/k ).each {|beishu|
#    0.upto(k-1).each {|index|
#        dp[beishu][index] = arr[beishu*k + index]
#    }
# }
# 
# 
# 
# dp.each
# 

# 
# 
# da = Array.new(n/k + 1) {Array.new(n+1,0)}
# da_inpu = Array.new(n+1) {Array.new(n+1,0)}
# 0.upto(n/k).each { |ks|
#    0.upto(k-1).each { |i|
#      da[ks]  <<  arr[ks*k + i]    if !arr[ks*k + i].nil?
#       }
#    }
# 
# 
# 1.upto(k).each {|co|
#    dp[1][co]
# }
# p dp 