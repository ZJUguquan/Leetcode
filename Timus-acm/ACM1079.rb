#  acm 1079
include Math

def findX(n)
  return Math.log(n,2).floor
end



def fibo(x)
  if x == 0 or x ==1 or x ==2
     return 1
   else
    return fibo(x-1) + fibo(x-2)
  end
end



#  using new X, insted of the n
#  the maximum value of  a[i], i = 1.. 2^x   is 
#  max = f(x)
#  f(1)=1     f(0)=1   
#    -> f[m] = f[m-1] + f[m-2]       
#    USE  LARGER  to  EXPRESS SMALLER 
#    think about m ,  try to use two numbers larger  to calculate
#    two even number : L = 2*p   M = 2*q
#    m = (L+M)/2   a[m]= a[L]+a[M]




def s(l,r,i, v1, v2)
  m = (l+r)/2
  if i == m  
    return (v1+v2)
  else
    return m( m, r, i, v1+v2,v2)
  end
end






0.upto(99).each{|i|
top[i]= a[0,i].max
}

k=0
b = [] 
where = [] 
while true
  n = gets.chomp.to_i
  if n == 0 
    break
  else
    b << n
    k += 1
  end
end
p b 
b.each {|e| puts top[e]}

# result = []

# for ii in 0..(k -1) 
#   max = 0
#   s = b[ii]
  

# }

# def rec(n)
#   if n == 0 
#     return 0
#   elsif n == 1 or n==2
#     return 1
  
#   else  # n >=2
#     if n % 2 == 0
#       return rec(n/2)
#     else
#       return rec( (n-1) /2 ) + rec( (n+1)/2) 
#     end
#   end

# end

# Max = Array.new(100000)
# Max[0] = 0
# chose=[]
# 1.upto(100000) {|e| 
#   chose << rec(e)
#   Max << chose.max

# }

# 1.upto(20) {
#   |e| puts e
# }
# puts rec(45)