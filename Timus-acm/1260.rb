# 1260  nudnik photographer 

n = gets.chomp!.to_i

def pern(n)
   if n == 1 or n == 2 
      return 1
   elsif n == 3
      return 2
   elsif n == 4
      return 4
   else
      return pern(n-1)+pern(n-3)+1 
   end
end

arr= [] ; arr[0] = 0; arr[1] = 1 ;arr[2]= 1; arr[3] = 2; arr[4] = 4; arr[5] = 6

out  = [] ; out[0] = 0
6.upto(55).each {|i| arr[i] = arr[i-1] + arr[i-3]+ 1}
#p arr 

puts arr[n]
#puts pern(n)      
      
      
=begin
The permutations are:

1 2 3 4 5
1 2 3 5 4
1 2 4 3 5
1 2 4 5 3
1 3 2 4 5
1 3 5 4 2

a[i-1] stands for the first four, beginning with '1 2'. If you ignore 1, you have the same prob for N=i-1.
a[i-3] stands for the fifth, beginning with '1 3 2 4'. If you ignore 1, 3, 2, you have the same prob for N=i-3.
And a special case (the last) -- all the odds in increasing order, followed by all the evens in decreasing order. The is what the +1 in the formula means.
  
=end    