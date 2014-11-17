# 1910 
n = gets.chomp!.to_i


a = gets.chomp!.split(" ").map {|x| x.to_i}
b = []
0.upto(n-3).each do |i|
   b << a[i]+a[i+1]+a[i+2]
end 
 print "#{b.max} #{b.rindex(b.max)+ 2}"
  
 


