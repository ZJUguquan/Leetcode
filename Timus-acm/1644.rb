# 1644 a whole lot of walnuts
n = gets.chomp!.to_i; h1 = {}; h2 ={}
1.upto(n).each do |i|
   m,state = gets.chomp!.split(" ")
   if state == "hungry"
      h1[m.to_i] = state
   else
      h2[m.to_i] = state
   end
end
hungry_max = h1.keys.max ; satisf_min = h2.keys.min

if h2.keys.empty?
   puts 10 
elsif h1.keys.empty?
   puts satisf_min
else

   if  hungry_max >=  satisf_min
      puts "Inconsistent"
   else
      puts satisf_min
   end
end