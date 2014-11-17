# 1104   Don't ask woman about her age
# 

# 
# 
# y =[] ; ys=""
# s ="A1A"
a = "" ; 
s = gets.chomp! ; p = 0 ; max = 0
s.each_char.to_a.each {|c| 
  if c.ord > 60
     c = c.ord - 55
     p += c
     max = c if c > max
  else #  0 .. 9
     p += c.to_i
     max = c.to_i if c.to_i > max 
  end 
}

if max == 0
   i = 0 ; print "2" 
else # max >=1
   i = max +1
   while i < 37 do
      if p % (i - 1) == 0 
         puts i; break
      end
      i += 1
   end
end

if (i==37) 
   puts "No solution."
end
 

