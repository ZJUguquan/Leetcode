# 1370 
n,m = gets.chomp!.split(" ").map {|x| x.to_i }
a = Array.new(n,0)
0.upto(n-1).each do |i| 
   s = gets.chomp!.to_i
   a[i] = s
end

res = a.rotate(m)[0,10]
res.each {|e| print e}


