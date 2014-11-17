# 1404 easy to hack

h={}; h = Hash[(Array 'a'..'z').zip(Array 0..25)] ;h_reverse = Hash[h.to_a.map {|x| x=x.reverse}]
input = gets.chomp! ;input_arr = input.each_char.to_a
step1 = []
input_arr.each {|e| step1 << h[e] }
 (step1.length-1).downto(1).each do |index|
   step1[index] -=  step1[index-1]
end
step1[0] -= 5 ;
step1.each {|e| print h_reverse[e.divmod(26)[1]] }

