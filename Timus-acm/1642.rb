# 1642  1D Maze
n, x = gets.chomp!.split(" ").map {|x| x=x.to_i}
#n : obstacles  x : exit point
# second line : obstacles 

obstacles_left = [] ; obstacles_right = []
obstacles = gets.chomp!.split(" ").map {|x| x=x.to_i}
obstacles.each {|e| 
   if e < 0 
      obstacles_left << e
   else
      obstacles_right << e  
   end
}
 left_nearest = obstacles_left.max ; right_nearest = obstacles_right.min
procimp = Proc.new { puts "Impossible"}
if  n ==0
   if x == 0
      print "0 0"
   else
      procimp.call
   end
else # N > 0
   if x == 0
      print "0 0"
   else
   ###########
#left empty 
      if obstacles_left.empty?
         if x < 0
            print "#{x.abs+right_nearest*2} #{x.abs}"
         else
         
               procimp.call
            # else
   #            
   #          end
         end
      
      
   # right empty
      elsif obstacles_right.empty?
         if x < 0
            procimp.call
         else # x > 0 
             print "#{x} #{x+left_nearest.abs * 2}"
          end
   # consider left, right both exist 
      else 
        
         nearest = left_nearest.abs < right_nearest ? -(left_nearest) : right_nearest 

     
         if x > 0 # exit
            if x > right_nearest 
               procimp.call
            else
               print "#{x} #{x+left_nearest.abs * 2} "
            end
         else # x<0     # both-ex   x< 0 
            if x < left_nearest
               procimp.call
            else   #   left.   x 
               print "#{x.abs+right_nearest*2} #{x.abs}"
            end
         end
      end
   end
end





