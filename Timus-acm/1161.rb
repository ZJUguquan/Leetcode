include Math
a=[]
n = gets.chomp!.to_i
1.upto(n).each do|temp|
   temp =gets.chomp!.to_i
   a << temp 
end
a=a.sort.reverse
0.upto(a.length-2).each  { |i| a[i+1]= 2*sqrt(a[i]*a[i+1]  )}
printf "%.2f" , a.last 
