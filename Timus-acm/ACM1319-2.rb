
def matrix(n)
  # paint the matrix n: integer
  ans = Array.new(n ,Array.new(n))
#  n = n + 1
  if n == 1 
    return 1
  else
    #for i in 1 .. n 
    #  ans[i][n]
    x = 1
    key = 2 * n
    k = 2
    while k <= key   
            for i in 1.. n  
              for j in 1.. n 
                      if i + j == k  
                        ans[i-1][j-1] = x
                        x += 1
                      end

       k += 1
    end
      return ans
  end
end
        


a = matrix(3)
p a 
