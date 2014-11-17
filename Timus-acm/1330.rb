# 1330 intervals
 arr = []; output = []; sum = 0 ; arr[0]= 0
 n = gets.chomp!.to_i
 1.upto(n).each { arr << sum += gets.chomp!.to_i }
 m=gets.chomp!.to_i 
 1.upto(m).each do |i|
    a, b = gets.chomp!.split(" ").map {|x| x=x.to_i}
    output << arr[b] - arr[a-1]
 end
 output.each {|o|  puts o }
 
 