# 1353 

# 10 digit   first cant zeros. 
# x1 x2 x3 +.... + x10 = S  x1 >=1  x2-10 >= 0 , < = 9
#  1 + 1 + 1 ....... +  1  (total s [1] s ) 0 <= xi <= 9   

def factorial(n) 
   if n == 0 or n == 1
      return 1
   else
    return (1..n).inject(:*)
   end
end

def combinator(n,k) ; return  factorial(n)/factorial(k)/factorial(n-k) ;end 
   


def allpos(s,digit)
   if s == 1
      return 10 
   else
      digit = 9
      return combinator(s+digit-1, s)
   end
end

def sumdigits(n)
   s = n.to_s.each_char.to_a.map(&:to_i)
   return s.inject(:+)
end
output = Array.new(82,0)

0.upto(9).each {|i1|
   0.upto(9).each {|i2|
      0.upto(9).each {|i3|
         0.upto(9).each {|i4|
            0.upto(9).each {|i5|
               0.upto(9).each {|i6|
                  0.upto(9).each {|i7|
                     0.upto(9).each {|i8|
                        0.upto(9).each {|i9|
                           output[i1+i2+i3+i4+i5+i6+i7+i8+i9] += 1
                        }
                     }
                  }
               }
            }
         }
      }
   }
}
p output

# 1.upto(10**8).each {|s|      output[sumdigits(s)] += 1}
# p output 
#p allpos(10,9)
   

=begin 
11 -> 75501
15 -> 478731
20 -> 2714319
45 -> 40051495
=end