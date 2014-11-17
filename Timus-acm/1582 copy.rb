# 1582 Bookmakers 
a1,a2,a3 = gets.chomp!.split(" ").map(&:to_f)
puts (1000*a2/(a2/a1+a2/a3+1)).round