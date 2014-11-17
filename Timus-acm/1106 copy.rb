#1106  two teams
teams = [] ;n = gets.chomp!.to_i ; left = []; right = []; teams[0]=0
1.upto(n).each {
   teams << gets.chomp!.split(" ").map {|x| x=x.to_i} -[0] 
}

1.upto(n).each do |i|
   if !left.include?(i) and !right.include?(i) # both not
      left << i
      # iterating his friends
      teams[i].each {|e| (right << e)  if !left.include?(e) and !right.include?(e)  }
   elsif left.include?(i)  # in left
       teams[i].each   {|e| (right << e)  if !left.include?(e) and !right.include?(e) }
   else
       right.include?(i) # in right
   end
end

p left.uniq.length
left.uniq.sort.each {|e| print "#{e} "}   
# puts 
# right.uniq.sort.each {|e| print "#{e} "}
 
=begin
7
2 3 0
3 1 0
1 2 4 5 0
3 0
3 0
7 0
6 0

=end