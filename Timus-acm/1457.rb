# 1457
n = gets.chomp!.to_f
a = gets.chomp!.split(" ").map {|x| x.to_i}
res = a.inject {|sum,e| sum+e}
printf "%6.6f",res/n 