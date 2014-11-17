#1228 array

n, k =gets.chomp!.split(" ").map(&:to_i)
a=[]
1.upto(n).each { a << gets.chomp!.to_i }


k -= 1 ; t = 0
while k != 0
   print "#{k/a[t]} "
   k = k % a[t]
   t +=1
end
