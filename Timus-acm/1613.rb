#1613 for fans of statistics 

=begin 
is there among the cities with numbers from l to r 
such that the trams of this city transported exactly x people during last year.

      if thisqu == sum
         ans = "1"
      else
         ans = "0"
      end
=end

n = gets.chomp!.to_i  
a = gets.chomp!.split(" ").map(&:to_i)
q = gets.chomp!.to_i
str= "" ;

1.upto(q).each {|i|
   left, right , sum = gets.chomp!.split(" ").map(&:to_i)
   if a[left-1] == sum  or a[right-1] ==sum   
      str+= "1" 
   else
      comp = a[left-1 .. right -1]
      comp.include?(sum)  ? str+= "1" :str+="0"
      #thisqu= arr([(left-1)..(right-1)]).inject(:+)  
      
   end
}
puts str