#  acm 1079

n = 999

def rec(n)
  if n == 0 
    return 0
  elsif n == 1 or n==2
    return 1
  
  else  # n >=2
    if n % 2 == 0
      return rec(n/2)
    else
      return rec( (n-1) /2 ) + rec( (n+1)/2) 
    end
  end

end

Max = Array.new(100000)
Max[0] = 0
chose=[]
1.upto(100000) {|e| 
  chose << rec(e)
  Max << chose.max

}

1.upto(20) {
  |e| puts e
}
# puts rec(45)