# 1446
n = gets.chomp!.to_i
h = {} ;  s1=[]; h2=[]; g3=[]; r4=[]
1.upto(n).each do |i|
   name = gets.chomp!
   coll = gets.chomp!
   case coll[0]
   when "S" 
      s1 << name 
   when "H"
      h2 << name
   when "G"
      g3 << name
   else
      r4 << name
   end
   h[name] = coll
end

puts "Slytherin:"
s1.each {|e| puts e}
puts "\nHufflepuff:"
h2.each {|e| puts e}
puts "\nGryffindor:"
g3.each {|e| puts e}
puts "\nRavenclaw:"
r4.each {|e| puts e}


#reversed_h = Hash[h.to_a.reverse]
#rh = Hash[h.values.zip(h.keys)]
#p rh
#p reversed_h

