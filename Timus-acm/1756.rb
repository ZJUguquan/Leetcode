# 1756   diggers

# m diggers can dig a trench in exactly d1 days if they all work every day. 
# Help Vitya compile a work schedule according to which a minimal number of diggers can dig a trench in exactly d2 days.
# 1 <=  ... <= 10 000
# input  m , d1, d2 

m , d1, d2  = gets.chomp!.split(" ").map(&:to_i) #  [3, 1, 2]

if d2 == 1 
   puts m*d1
elsif d2 == d1
   1.upto(d1).each {|e|  print "#{m} "}
   
else#if d2 < d1 
   total =  m * d1  # integer
   div = total / d2 
   cha = [] ; minidigger = 0 ; less = 0 
   (div).upto( (total+d1+d2)/d2).each {|i|    cha << te =i * d2 - total
      if te >= 0 
         minidigger = i
         less = cha.pop
         break
      end
   }
  # p minidigger ; p less

   ans = []  ; ans << minidigger
   
   1.upto(d2-1).each {|e|  ans << (minidigger-1) }
   temptotal = ans.inject(:+)
   1.upto(total - temptotal ).each {|e| ans[e] +=1}
   # p ans
 #   p temptotal = ans.inject(:+)
   ans.each {|e| print "#{e} "}
end
   

=begin
5 2 3 -> 3 3 4

5 6 4 -> 7 7 8 8 

=end