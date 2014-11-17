# 1283
n,m,c = gets.chomp!.split(" ").map(&:to_i)
#p n,m,c
years = 0
if n <= m
   puts 0
else

      while n > m
         n = (100-c)/(100.to_f) * n
         years += 1
      end
      puts years
end