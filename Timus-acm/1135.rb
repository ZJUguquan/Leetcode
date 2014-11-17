# 1135 
n = gets.chomp!.to_i

s =""; 

while s.length < n and line = STDIN.gets
   s = s.delete("\n")
  # if s.length < n
     s += line if line.include?(">") or line.include? "<"

     
end
s= s.delete("\n") 
count = 0
while s.include? ("><")
   
   s=s.sub("><","<>")
   count += 1
  # p s
end

puts count



=begin
STDIN.each do |str|
  str.chomp!
  puts "String: #{str}"
end
=end
