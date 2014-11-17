# 1206  sum of digits  of the sum of numbers 

k = gets.chomp!.to_i
puts 36 * 55**(k-1)




def digitsum(a)
   a.to_s.each_char.to_a.map(&:to_i).inject(:+)
end



test = 123123
p test.to_s.each_char.to_a.map(&:to_i)

p digitsum(1298) # => 
# ~> -:4:in `map': wrong number of arguments (1 for 0) (ArgumentError)
# ~> 	from -:4:in `digitsum'
# ~> 	from -:7:in `<main>'
