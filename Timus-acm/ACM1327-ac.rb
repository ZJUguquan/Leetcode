# 1327
# 
a=gets.chomp.to_i
b=gets.chomp.to_i
res = (b-a+1)/2
res += 1 if b%2==1 and a%2==1 
puts res 

