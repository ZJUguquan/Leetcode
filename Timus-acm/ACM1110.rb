#  ACM 1110
# input n M -1  y 
#  find all numbers x in [0, M-1] 
#   x^N  mod M = Y 

input = gets.chomp.split(" ")
$n=input[0].to_i
$m=input[1].to_i
$y=input[2].to_i
$output = []


def fmx(x,y)    #  x^n % m 
  #  f(N) = x^N % M = Y 
  #    x^ N = K*M + Y 
   # f(N+1) =  x^(N+1) mod M = (km+Y)x mod M 
   #  = yx mod M  = f(n) x mod M 
   #      
   #  x^(N) * x  mode  M 
   if y == 1
     return x 
   elsif   

end

=begin
   
=end


for x in 0..(m-1) 
  $output <<  if x ==0 and $y ==1

  
  output << x if x **n % m == y  
end

    # if  Math.power(x, n) % m == y 
    #     output << x
    # end
output.each{
 |e| print "#{e} " 
}


#p output 