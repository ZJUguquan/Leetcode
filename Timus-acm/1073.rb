# 1073
def sign(n)
   if n > 0
      return 1
   elsif n==0
      return 0
   else 
      return -1
   end
end
#n = gets.chomp!.to_i
n = 310
0.upto(Math.sqrt(n).floor).each {|i1|
   0.upto(Math.sqrt(n).floor).each {|i2|
       0.upto(Math.sqrt(n).floor).each {|i3|
           0.upto(Math.sqrt(n).floor).each {|i4|
              if i1*i1 + i2*i2 +i3*i3 + i4*i4 == n
                 puts sign(i1)+sign(i2)+sign(i3)+sign(i4)
                 puts "#{i1} #{i2} #{i3} #{i4}"
              end
           }
        }
     }
}

# 
# def f(n)
#    2.upto(n).each {|i| 
#       1.upto(Math.sqrt(n).floor).each {|j|
#          min = f(i - j*j)  if min > f[i- j*j]
#       }
#       f(i) = min + 1
#    }