# 1617 flat spots

 n=gets.chomp!.to_i
 a=[]
 1.upto(n) { |line|  a << line =gets.chomp!.to_i } 
m = Hash.new
a.uniq.each do |e|
   m[e] = a.count(e)
end
sum = 0 
m.each { |k,v|      sum += v/4 }
 
 p sum  
 
  # wh = STDIN.read.split("\n").map {|x| x.to_i }