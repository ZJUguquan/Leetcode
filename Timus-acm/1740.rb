# 1740 Deer is better 

l, k,h =gets.chomp!.split(" ").map(&:to_i)
hs = h * (l/k)

if  l % k == 0
   printf "%5.6f %5.6f" ,hs,hs
else
   printf "%5.6f %5.6f" ,hs,hs+h
end
