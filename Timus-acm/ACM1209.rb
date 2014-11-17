# ACM 1209
# 
include Math
# N  
number = gets.chomp.to_i 
number = number.to_i
result = [] 


# generate the sequence
 
 i = 1
 xuhao = [] 
 result = " "
 cursor = 1

def is_special?(k)
  t = Math.sqrt(8 * k -7 )
  t2 = t.floor
  if t == t2
      return true
  else
    return false
  end
end




i = 0 
output =""
while i < number 
  temp = gets.chomp!
  temp = temp.to_i
  if is_special?(temp)
    output += "1 "
  else
    output += "0 "
  end
  i +=1
end

puts output   


=begin
  
rescue Exception => e
  
end
# while i < 31
#   temp = (i + 1) * (i - 2) / 2 + 2 
#   xuhao << temp
#   i += 1
# end
def is_special?(n)
  i = 2
  while i < 2**15
    if n == (i + 1) * (i - 2) / 2 + 2 
      return true
    end 
      i += 1
    end
    return false
end
# result2 = result.each_char.to_a

=end