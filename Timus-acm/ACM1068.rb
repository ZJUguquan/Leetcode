# ruby

number = gets.chomp!
number = number.to_i

# number = -3

if number == 1                    #       number.abs > 10000   
  puts 1
elsif number < 1
  sum = 0
  for i in number .. 1
    sum += i 
  end
  puts sum
else
  sum = 0
  for i in 1 .. number
     sum += i 
  end
  puts sum
end

  
