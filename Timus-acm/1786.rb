# 1786 
out = [] ;inp = gets.chomp!.each_char.to_a ;
target = "Sandro"

def string_difference(a,b)    # different with "sandro" b, put b.  
   a = a[0,6];   res = 0;  # res: similarity 
   case a[0]
   when "S"
      res += 2
   when "A".."R", "T".."Z", "s"
      res += 1
   else
   end
   1.upto(5).each {|index|
       if b[index] == a[index] 
          res += 2
       elsif
          a[index].downcase == b[index] or ("a".."z").cover?a[index] 
          res += 1
       else
       end 
       }
   return 12-res # change cost. 
end

0.upto(inp.length-6).each do |i|
   out << string_difference(inp.rotate(i),target)
end
 puts (out.min) * 5
  
 
# p string_difference(a2,target)


# a=[]
# a[1] = "Sandro" ; a[2]="sandro"
# a[3] ="xander" ; a[4]="asdfRO"; a[5]="adfdrop"
# a[6] = "ZZZZZZ"
# 1.upto(6).each {|i| 
#    p string_difference(a[i],target)}

=begin
def string_difference_percent(a, b)
  longer = [a.size, b.size].max
  same = a.each_char.zip(b.each_char).select { |a,b| a == b }.size
  (longer - same) / a.size.to_f
end
=end
