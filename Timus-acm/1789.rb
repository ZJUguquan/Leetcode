# 1789  searching for the dodecahedron

# n = gets.chomp!.to_i
n=4
m = 2 * n - 1

case n 
when 2, 3
   print "2\n 2 2"

puts 2*n-1
1.upto(n).each {|i| print "#{i} "}
n.downto(2).each {|i| print "#{i} "}

# 
# n=3
# 2 2
# 
# n=4
# 2

n = gets.chomp!.to_i
puts 2*n-1
1.upto(n).each {|i| print "#{i} "}
n.downto(2).each {|i| print "#{i} "}