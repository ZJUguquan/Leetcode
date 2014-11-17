# 1880 
h = Hash.new 
m = gets.chomp!.to_i
line1 = gets.chomp!.split(" ").map {|x| x.to_i}
line1.uniq.each {|i| h[i] = 1}
n = gets.chomp!.to_i
line2 = gets.chomp!.split(" ").map {|x| x.to_i}
line2.uniq.each_with_index {|e|
   h[e] += 1 if h.has_key?(e) 
}
p = gets.chomp!.to_i
line3 = gets.chomp!.split(" ").map {|x| x.to_i}
line3.uniq.each { |e|
   h[e] += 1 if h.has_key?(e) 
}
puts h.values.select {|x| x > 2 }.count 