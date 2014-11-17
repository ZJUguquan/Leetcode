#  ACM 1712  cipher grille

a = Array.new(Array.new)
line =[]
i = 1
while i <= 4
  temp = gets.chomp!
  temp.each_char {|c|  a[i-1] << c }
  i += 1
end

p a 
