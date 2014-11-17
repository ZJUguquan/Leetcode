# acm1083  factorials
input = gets.chomp!

ins = input.each_char.to_a
if ins[1]= '0' 
   m = 10
   n = input.length - 3
else 
   m = ins[0].to_i
   n = input.length - 2
end




def factorial(m)
  if m==1 or m==0 
    return 1
  else
    return factorial(m-1) * m 
  end
end

def factorials(m,n)
  if m ==0  or m==1 
    return 1
  end
  if n == 1
    return factorial(m)
  end
  if n >= 2
    if m%n == 0
     prod = 1
     for i in 1..(m / n)
        prod = prod * n * i
     end 
     return prod

   else # m % n >=1
      qu = m / n 
      if qu > 0 
                re = m - qu * n 
                prod = n
                for i in 1 .. qu
                  prod = prod * (prod -  (i * n) )
                end
                return prod
      else # qu=0
        return m
      end
    end
  end
end
puts factorials(m,n)


