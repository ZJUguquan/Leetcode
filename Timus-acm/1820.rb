# 1820 

n, k = gets.chomp!.split(" ").map {|x| x.to_i }
res = n / k + 1 + (n - 1 + n% k )/ k 
#(k >= n) ? 2 : (n * 2 / k   +  (n%k ==0 ? 0 : 1) ) 
puts n<= k ? 2 : res 