
# 1225
# 
# 


a = Array.new(46)

a[1] = 2
a[2] = 2
# has blue 
a[3] = 4

4.upto(45).each {|e|
    a[e] = a[e-1] + a[e-2]
}
n = gets.chomp.to_i
puts a[n]




puts "0000".."9999"