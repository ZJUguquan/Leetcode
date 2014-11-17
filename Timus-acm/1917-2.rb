# 1917 -2   
$n, p =  gets.chomp!.split(" ").map(&:to_i)
def count(a, val)
   num = 0; 
   0.upto($n - 1).each {|i|   num += 1 if a[i] <= val and a[i] != 0      }
   return num
end

def asign(a, val)
   0.upto($n - 1).each {|i| a[i] = 0 if a[i] <= val}
end

arr = gets.chomp!.split(" ").map(&:to_i).sort
sum = 0; magic_sum = 0 ; t = -1
while(true)
   0.upto($n-1).each {|i|
      cnt = count(arr,arr[i])
      if arr[i] !=0 and arr[i] * cnt <= p
         sum += cnt # damaged coins stat
         asign(arr, arr[i])
         magic_sum += 1
      end
      while arr[i] == arr[i+1] and i < $n
         i += 1
      end
   }
   if t == sum
      break; 
   end
   t = sum 
end

print "#{sum} #{magic_sum}"
