#
$a = 1
$b = -2
$c = 1
def fx(x,time,a=$a,b=$b,c=$c)
  #a,b,c= $a,$b,$c
  x= x+time
  a*x*x + b*x +c 
end

def total_distance(n)
  sum = 0 
   1.upto(n).each {|i|
    sum +=  fx(x,i-1)
   }
   sum
 end

 i =1

 while i <10000  
    if total_distance(i) == 0
      puts n 
       break
    else
      i +=1 
    end
  
  end


  
 




# def direction(f)
#   if f > 0 
#     return 1
#   else
#     return -1
#   end
# end