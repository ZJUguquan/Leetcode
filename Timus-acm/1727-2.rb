# 1727  znika's magic numbers

#k = gets.chomp!.to_i
k = 17 
a = Array 1..9999



def countsumdigt(s)
   a = s.to_s.each_char.map(&:to_i) 
   return a.inject(:+)
end
p1 = 
#p countsumdigt 12
#
b =[] ; a.each {|e| b<<countsumdigt(e)}
h = Hash[a.zip(b)]


couser = 0 ; diff =  k - couser
while (diff > 10)
  couser =  
