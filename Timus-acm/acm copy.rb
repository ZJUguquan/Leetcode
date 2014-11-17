# acm    1014 
include Math

def prime(n)
  # if prime return 1  else  , all  2 factors. 
  sqr = Math.sqrt(n).floor
  i = 2 
  heshu = false
  while i < sqr 
    if n % i == 0 
      qur = n / i 
      result = i.to_s + qur.to_s
      heshu = true
      return result.to_i 
    else 
      i += 1
    end
  end

  if heshu == false 
    return -1
  end

end

number = gets.chomp!
number = number.to_i
puts prime(number)
#puts Math.sqrt(101)