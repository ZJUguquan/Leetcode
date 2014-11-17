# 1725 sold out


n, k = gets.chomp!.split(" ").map(&:to_i)
if n== 2
   puts 0
else
   if k <= n/2
      puts (n-k-2)
   else # k > n/2
      k = n - k + 1
      puts  (n - k -2)
   end
end     