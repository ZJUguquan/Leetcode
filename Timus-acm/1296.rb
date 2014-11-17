# 1296 hyperjump
n = gets.chomp!.to_i ; 
sum = 0 ; max1 = 0
1.upto(n).each { |e|    e = gets.chomp!.to_i
   sum += e
   sum = 0 if (sum < 0)
   max1 = sum > max1 ?  sum : max1
}
puts max1 