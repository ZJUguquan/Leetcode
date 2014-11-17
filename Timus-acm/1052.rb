#1052 Rabbit hunt

# check 3 poinds  online?
# class node
#    atr 
#    @x,@y
# end

def cross (a, b, c)
   return (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])
end
n = gets.chomp!.to_i
points = Array.new(n){Array.new(n,0)}

0.upto(n-1).each {|i|
   points[i] = gets.chomp!.split(" ").map(&:to_i)
}

ans = -1 ; m = 0 ; 
0.upto(n-1).each {|i|
   (i+1).upto(n-1).each {|j|
      m = 2; 
      (j+1).upto(n-1).each {|k|
         if cross(points[k],points[i],points[j]) == 0
            m += 1 ; #puts "asdlfkja"
         end
      }
      ans =  m  if  ans < m 
   }
}

p ans
