# 1944  Record of the attack at the orbit 

n = gets.chomp!.to_i
ps_x = [] ; ps_y = [] ; 
points = Array.new(201) {Array.new(201){}}


if n == 1
  x, y = gets.chomp!.split(" ").map(&:to_i)
  points[x+100][y+100] = 2 ; x += 100 ; y += 100 
  if x == 100 and y == 100 
    print "+"
  else 
    left = [100,x].min ;  right = [100,x].max
    bot = [100,y].min ; top = [100,y].max
  #  p [left,right,top,bot]
  end

else # n > 2
1.upto(n).each {|i|
  x,y = gets.chomp!.split(" ").map(&:to_i)
  x+= 100 ; y += 100
  points[x][y] =  9
  # left = x if x < left 
  # right = x if x > right
  # top = y if y > top 
  # bottom  = y if y < bottom
  ps_x <<  x;  ps_y << y; 
}

left = [ps_x.min,100].min; 
right = [ps_x.max,100].max; 
bot = [ps_y.min,100].min; 
top = [ps_y.max,100].max
end

#
(top).downto(bot).each {|y|
  (left).upto(right).each {|x|
      if !points[x][y].nil? 
        print "*"
      else
        if x != 100 and y == 100
          print "-"
        elsif x == 100 and y != 100 
          print "|"
        elsif x == 100 and y == 100
          print "+"
        else
          print "."
        end
      end
    }
    puts
  }

