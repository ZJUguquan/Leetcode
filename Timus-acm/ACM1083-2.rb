# acm1083  factorials
input = gets.chomp!

ins = input.each_char.to_a
if input.include? "0" 
   $n = 10
   $k = input.length - 3
else 
   $n = ins[0].to_i
   $k = input.length - 2 
end

def factor(n)
   if n == 1
      return 1
   else 
      return factor(n-1) * n
   end
end

def calculate(n, k)
   if n == 1
      return 1
   end
   if k == 1
      return factor(n)
   else # k > = 2
      if n <= k
         return n
      else
      
         if n  % k == 0
            qu = n / k 
            return factor(qu) * k**qu
         else # have reminder
            qu = n/k
            reminder = n - (n/k)*k
            prod = 1
            for i in 0 .. qu
               prod = prod * (reminder + k * i)
            end 
            return prod
         end
      end
   end 
end

puts calculate($n,$k)