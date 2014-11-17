#1545  hieroglyphs
n = gets.chomp!.to_i
re = []
1.upto(n).each {|e|
   e = gets.chomp!
    re << e}

k = gets.chomp!
re.each do |e|
   if e[0] == k
      puts e
   end
end

