#  acm 1214 String procedure

#N, K = gets.chomp.split(" ").collect {|x| x.to_i}

n = 1 , k =1
def ppp(x,y)
  if x>0 and y>0
    1.upto(x+y).each {|i|
       y =x*x +y 
       x = x*x+y
       y =Math.sqrt(x+ y/y.abs)*(-y.abs) 
       1.upto(2*y) {|j|    x = x-y }
     }
  end
  res=[x,y]
  return res
end
    

p ppp(1,1)
#print "#{N} #{K}"