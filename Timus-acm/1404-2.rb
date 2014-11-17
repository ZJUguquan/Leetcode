# 1404 -2  easy to hack

h={}; h = Hash[(Array 'a'..'z').zip(Array 0..25)] ;h_reverse = Hash[h.to_a.map {|x| x=x.reverse}]
#input = gets.chomp!
input ="secret" ; input_arr = input.each_char.to_a
# step1
step1 = []
input_arr.each {|e| step1 << h[e] }

step1[0] += 5 ;

 1.upto(step1.length-1).each do |index|
  # step1[index] += 26
   step1[index] = step1[index] + step1[index-1]
  step1[index]=  step1[index]>26 ? step1[index].divmod(26)[1] : step1[index] 
end
p step1


step1.each {|e| print h_reverse[e]}
# step1.each {|e| print h_reverse[e.divmod(26)[1]] }

