# 1222
n = gets.chomp!.to_i

if n ==1
   res = 1
elsif n==2
   res = 2
else 
   if n % 3 == 0
      res = 3**(n/3)
   elsif n % 3 == 2
      c = (n-2) / 3
      res = 3**(c)*2
   else # n % 3 = 1 
      c = (n-4)/3
      res = 3**(c) *4
   end
end
puts res