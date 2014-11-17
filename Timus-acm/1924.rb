# 1924 four imps

# grimy  odd 
# black  even 
 n = gets.chomp!.to_i
 res = 1
if n >=3 then   2.upto(n).each {|i|   res = res + i * (-1)**i }  end
puts  res % 2 ==1 ? "grimy" : "black" 