# 1636

t1,t2 = gets.chomp!.split(" ").map {|x| x=x.to_i}
n = gets.chomp!.split(" ").map {|x| x=x.to_i }
sum = 0
sum = n.inject(:+)  

t2 -= sum * 20 
puts   t2 < t1 ?    "Dirty debug :(" : "No chance." 

