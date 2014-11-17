# 1788  on the benefits of umbrellas
def conduct(girls,boys,aco)  # aco <= min(girls, boys)
   girls = girls.sort.reverse; boys = boys.sort.reverse
   total = 0 ; gl = girls.length  ;  bl= boys.length ; smaller = gl < bl ? gl : bl
   if  aco ==0
      total = girls.inject(:+)
      return total
   elsif aco == 1
      1.upto(gl-1).each {|index| total += girls[index]}
      1.upto(bl-1).each {|index| total += boys[index]}
      return total
   elsif aco == smaller 
      if bl > smaller 
         gl.upto(bl-1).each {|e| total += boys[e]}
         return gl * total
      else # girls larger
         bl.upto(gl-1).each {|e| total += girls[e]}
         return total
      end
   else # aco  mid. 
      girlsupset = 0 
      aco.upto(gl-1).each {|e|  girlsupset += girls[e]}
      boysupset = 0 
      aco.upto(bl-1).each {|e| boysupset += boys[e]}
      total = girlsupset + aco * boysupset
      return total
   end
end
def whichacoosmall(girls,boys)
   gl = girls.length  ;  bl= boys.length ; smaller = gl < bl ? gl : bl
   mins = [] # conduct(girls,boys,0); 
   0.upto(smaller).each {|i|
     
         mins << conduct(girls,boys,i) 
         #print  "#{mins} #{i} accc\n"
     
   }
 #  p mins
   return mins.min
end
# count  
girls, boys  = gets.chomp!.split(" ").map(&:to_i)
girlsupset = gets.chomp!.split(" ").map(&:to_i)
boysupset = gets.chomp!.split(" ").map(&:to_i)

if girls == boys 
   puts 0
else
   puts whichacoosmall(girlsupset, boysupset)
end

# p conduct(girlsupset, boysupset,0)
# p conduct(girlsupset, boysupset, 1)
# p conduct(girlsupset,boysupset, 2)
# p whichacoosmall(girlsupset,boysupset)


