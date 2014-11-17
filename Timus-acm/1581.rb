# 1581 Teamwork
n = gets.chomp!.to_i
sum = 1
m = STDIN.read.split(" ").map {|x| x.to_i }
start = m[0]
1.upto(n-1).each do |i|
   if m[i] == start
      sum +=1
   else
      printf "%d %d ", sum ,start
      start = m[i]
      sum = 1
   end
end
printf "%d %d", sum, start 


       
   


# 
# def printNum(a)
#    print "#{a.length} #{a[0]}"
# end
# 
# printNum "222"
# 
# s.count(10) # => 2
# b = Array.new(s.length,1)
# h = {}
# h = Hash[s.zip(b)]
# p h 
# h.keys.each {|k| h[k] = s.count(k) }
# >> {1=>1, 2=>1, 3=>1, 10=>1}
