# 1731n=2;m=3
n,m = gets.chomp!.split(" ").map(&:to_i)
1.upto(n).each {|i|print("#{i} ")}
puts
(n+1).upto(n+m).each {|i| print("#{i*n} ")}
