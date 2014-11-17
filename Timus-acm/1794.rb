# 1794 masterpieces of world architecture 
# the children speak  one after another in clockwise order 

# know each students needs   # give orders 
# who will be first 
# st. as many children as possiable will have their turn to speak exactly as they want. 

n = gets.chomp!.to_i
#a=[1, 2, 3, 5, 5, 6, 7, 8]
a =gets.chomp!.split(" ").map(&:to_i) #[3,3,1,5,5] ; 

votes = Array.new(n, 0) ; 
a.each_with_index do |e,i|
   votes[i - (e-1) ] += 1
end

puts 1+votes.index(votes.max)
   
   
   #p votes