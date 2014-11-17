# 1200 horns and hoofs 
# profit :   horns: A    hooff: B 
# produced amount (total) <= K   / per month 
# tax = amount**2

# input 
# first line : A B   two digits 
# 2nd line   K 

# output 
#maximal possible profit wit two digits precision
# second line:  optimal productionvolums 


a,b = gets.chomp!.split(" ").map(&:to_f)  
k = gets.chomp!.to_i    #  45
profits = 0; 
x = 0; y = 0 ; 
while  x+y < k
   dl_a =a -(2*x+1) ; dl_b = b-(2*y+1) ; mmm = [dl_a,dl_b,0].max 
   if dl_a == mmm and mmm> 0.0000001
      x += 1; 
      
   elsif dl_b == mmm and mmm> 0.0000001
      y += 1      
   else    
      break
   end
end

profit = -x*x-y*y+x*a+y*b
printf "%.2f\n",profit
print "#{x} #{y}"


