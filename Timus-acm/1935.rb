# 1935  Tears of Drowned 
# 6
# 1 3 2 5 4 6             27

n = gets.chomp!.to_i # 

# output the minimal required number of sheets in the book

line = gets.chomp!.split(" ").map {|x| x = x.to_i}
max = line.max
puts res = line.inject(:+) + max

