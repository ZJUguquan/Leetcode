# 1638 bookworm

a1,a2,n1,n2 = gets.chomp!.split(" ").map {|x| x=x.to_i}

puts ((a1+a2*2) *(n2-n1) - a1).abs

# a1: thickness of each v
# a2: thickness of each cover
# n1: number of volume from which the worm 
# n2: number of volume where it stopped 
#  input example  10 1 1 2 = > 2 
# output : length of the worm's route 
