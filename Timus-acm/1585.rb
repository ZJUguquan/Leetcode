# 1585
n=gets.chomp!.to_i
b = Array.new(3,0)
1.upto(n).each do |line|
   line = gets.chomp!
   case line[0]
   when "E" 
      b[0] += 1
   when "M"
      b[1] += 1
   else
      b[2] += 1
   end
   
end

case b.rindex(b.max) 
when 0
   puts "Emperor Penguin"
when 1
   puts "Macaroni Penguin"
else
   puts "Little Penguin"
end
