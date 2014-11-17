# 1423 String Tale  string algorhim
n = gets.chomp!.to_i
s= gets.chomp!
s2 = gets.chomp!

s =s +s
where = s.index(s2)
if where.nil?
   puts -1
elsif where == n
   puts 0
else
   puts n-s.index(s2)
end



# 
#   #"abracadabra"
#   have = false
#   1.upto(n).each {|index| 
#      s = s.split("").rotate().join("")
#      if  s == s2 
#         puts n-index
#         have = true
#         break
#      end
# }
# puts (-1)  if have ==false
