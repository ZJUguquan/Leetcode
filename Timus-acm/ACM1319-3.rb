
# n= gets.chomp!
# n= n.to_i

def matrix(n)
  # paint the matrix n: integer
  ans = Array.new(n) { Array.new(n) }
#  n = n + 1
  if n == 1 
    return 1
  else
    #for i in 1 .. n 
    #  ans[i][n]
   k = 0
    p = n - 1
    s = 0 
    while s <= (2*n -1)  
            for i in 1 .. (n  )  do 
                for j in 1 .. (n )  do 
                                          if j - i == p  
                                            #   右上角 
                                                            k += 1
                                                            ans[i-1][j-1] = k
                                          end

                                          
                 end

            end
    p -= 1     
    s += 1
    end
      return ans
  end
end
        

n=3
a = matrix(n)

for i in 0..(n-1)
  for j in 0..(n-1)
    print "#{a[i][j]} "
    puts 
  end
end
