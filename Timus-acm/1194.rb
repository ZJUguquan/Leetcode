# 1194

n,k = gets.chomp!.split(" ").map {|x| x.to_i}
res =  n*(n-1)/2- k
puts res