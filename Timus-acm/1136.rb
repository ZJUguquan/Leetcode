# 1136 Parliament

$a = [] ; $b =[]; 
def rec(x,y)
   if x < y 
      return
   end
   $b[$k] = $a[x]   ; $k += 1
   (x-1).upto(y).each {|i|
      if $a[i] < $a[x]
         rec(i,y)
         rec(x-1, i+1)
         return
      end
   }
   rec(x-1,y)
end

n = gets.chomp!.to_i ; $k=0

$a = gets.chomp!.split(" ").map(&:to_i)
rec(n-1,0)
(n-1).downto(0).each {|j|  print "#{$b[j]} " }
