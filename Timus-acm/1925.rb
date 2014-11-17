# 1925 british scientists save the world

n,k = gets.chomp!.split(" ").map {|x| x=x.to_i }
sum1=[]; sum2 =[]; a1,a2= 0
# enter number  <   X /2
n.times do |i|
   a1,a2= gets.chomp!.split(" ").map {|x| x=x.to_i }
   sum1 << a1; sum2 << a2
end
s1 = sum1.inject(:+)
s2 = sum2.inject(:+)
ans = s1 + k -(n+1)*2 -s2
puts  ans <= 0 ? :"Big Bang!" : ans 


=begin
6 5
3 1
3 1
5 3
6 5
5 5
7 2
=end