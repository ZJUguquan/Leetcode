# 1496 Spammer
n = gets.chomp!.to_i
a = []; h = {}
1.upto(n).each do |i|
    a << s = gets.chomp!  
 end
 
 a.uniq.each  { |e|    puts e if a.count(e) > 1 }
    
  # 
 # h.each do |k,v|
 #    puts k if v >= 2
 # end
 # 
 # h[s] = 1 if ?h.has_key(s)
 # h[s] += 1 if h.has_key(s)