

# n = gets.chomp.to_i
# n /= 2

n = 4      #  half string length 
k_m = 9 * n    # the biggest sum of half 
s = 0





def K(sum, n)
  m = Array.new(sum+1)
  0.upto(sum).each {|i| 
  if i > 9 
    m[i] = 0  
  else
    m[i] = 1
  end
  }
  1.upto(n-1).each {|j| 
    sum.downto(0).each {|i| 
      zz = 0
      if i > 9 
        zz = i - 9 
      end
      zz.upto(i).each {|z| m[i] += m[z] }
    }
  }
  return m[sum]
end


count = 0
0.upto(9*n).each { |sum|
  k = K(sum,n)
  count += k * k

}
puts count 


