#1510 order

n  =  gets.chomp!.to_i
arr = [] ；arr[0] = gets.chomp!.to_i ; 
$pointer = arr[0] ; $count = 1
if n == 1
   puts arr[0]
else   
   1.upto(n-1).each {|index|
      arr << temp = gets.chomp!.to_i
     
      if temp == arr[index-1]
         $pointer = temp
          $count += 1
      else
         
         if $count == 0 
            $pointer = temp
         end
         $count  -= 1
         
      end
   }
end

puts $pointer
