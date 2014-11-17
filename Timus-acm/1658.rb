# 1658  sum of digits 
# i can solve it brutely,  but there is 2 .0 second time limit. 
include Math
t= gets.chomp!.to_i

i= 1 
while i <= t 
   

a, b = 6 , 6

sum_squired = sqrt(b) 

sum_floor = sum_squired.floor


def powDigits(num, power = 1)
    num.to_s.split(//).inject(0) {|z, x| z + (x.to_i)**power}
end
solution = []
1.upto(1000000).each do |n|
if powDigits(n) == a and powDigits(n,2) ==b 
   solution << n 
   break
end
end


if  solution.length>=1 
   puts solution[0] 
else 
   puts "No solution"
end
   




 
 


 def sumDigits(num, base = 10)
     num.to_s(base).split(//).inject(0) {|z, x| z + x.to_i(base)}
 end




# 
# def sp(i)
#     ((1..9).to_a<<0).permutation(i).to_a.each do |x|
#        if x.inject(:+) == a
#           p x
#        end
#     end
#  end
#  
#  sp(2)


# 水仙花数 

# 
# def sp_num(i)
#     ((1..9).to_a<<0).permutation(i).to_a.each do |x|
#      sum = 0;mu =i-1;x.each {|v|sum+=v*10**mu;mu-=1};tmp=x.map {|i| i**3};p x if tmp.reduce(:+)==sum end
# end;
# 
# sp_num(3)



# 
# if sum_squired == sum_floor
#    puts "can be sol"
#    
#    
# else
#    puts "no solution"
# end
# 
# 
# 
# 
# p sum_squired.is_a?(Integer) #=>
# p a 
# p sum_squired