# acm 1197 
# lonesome kngiht

#

number = gets.chomp!
number = number.to_i
result = [] 

i = 0 
while i < number 
  temp = gets.chomp!
  result << temp
  i += 1 
end


def possiblities(input)
  inputs = input.each_char.to_a
  first = inputs[0]
  second = inputs[1]
  case first
  when "a","h"
    case second 
    when "1", "8"
      return 2
    when "2", "7"
      return 3
    else
      return 4
    end
  when "b","g"
    case second 
    when "1", "8"
      return 3
    when "2", "7"
      return 4
    else
      return 6
    end
  else
    case second 
    when "1", "8"
      return 4
    when "2", "7"
      return 6
    else
      return 8
    end
  end
end

   
result.each {|r| 
  puts possiblities(r)
}