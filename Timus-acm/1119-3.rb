# 1119 metro
# finals before? 
n,m =gets.chomp!.split(" ").map(&:to_i)
k = gets.chomp!.to_i 
$path =[]  
$board = Array.new(n+1){Array.new(m+1,0)}
1.upto(k).each {|e|   $path = gets.chomp!.split(" ").map(&:to_i)}

def min(x,y) ;   return x > y ? y : x     end
def shortest(n,m)
   if n == 0 and m == = 
      return 0
   elsif n<= 1 and m<=100
      return 100
   else
      temp = min(shortest(n-1,m),shortest(n,m-1)) + 100
      if $path.include?([n,m])
         return min(shortest(n-1,m-1)+ Math.sqrt(2)*100, temp)
      else
         return temp
      end
   end
end
puts shortest(n,m).round
    