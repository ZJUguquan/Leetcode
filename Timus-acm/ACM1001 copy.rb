# problem set 1001 
include Math

numbers = [] 
STDIN.read.split(/\W+/).each  { |a|
   puts a
   numbers << a.to_i
}


reversed_array = numbers.reverse

reversed_array.each {|e| 
  puts Math.sqrt(e)
}



# office 
tokens = []
while string = gets do
   string.split().each do |token|
      tokens << token
   end
end
tokens.reverse.each do |token|
   puts (token.to_i ** 0.5).round(4) 
end