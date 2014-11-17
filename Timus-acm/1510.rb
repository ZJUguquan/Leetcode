#1510 order

n  =  gets.chomp!.to_i
arr = [];arr[0] = gets.chomp!.to_i ; 
$pointer = arr[0] ; $count = 1
if n == 1
   puts $pointer
else   
   1.upto(n-1).each {|index|
      arr << temp = gets.chomp!.to_i  
      if temp == arr[index-1]
         if $count > 0
            if temp == $pointer
               $count += 1        # up
            else
               $count -= 1    # down
            end
         else  # $count = 0 
            $count += 1
            $pointer = temp
         end
      
      else  # different with last 
         
         if $count > 0
            $count -= 1
         else  # #count = 0 
            $count = 1
            $pointer = temp
         end
      
      end
   }
end

puts $pointer


=begin
   p "cpusdaf #{$count}"
5
5
5
3

=end
