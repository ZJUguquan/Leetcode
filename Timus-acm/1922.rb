#1922 superhero team
# reliable team: 
#  some heros need 3 teanmates,  some just himself
# know:  heros work at least X number 
# effectve : satisfies whishes of every superhero . 
# effective: add any other hero do ineffective 

n = gets.chomp!.to_i
a = Array.new(n+1) ; 
1.upto(n).each {|i| a[i] = Array.new}
h = {} ;  
h_count =  Hash[(Array 1.to_s..n.to_s).zip(Array.new(n,0))]
h_member =  Hash[(Array 1.to_s..n.to_s).zip(Array.new(n){[]})]

1.upto(n).each {|i|
      heneeds = gets.chomp!    
       # if h_count.keys.include? heneeds
     if h_member.keys.include? heneeds
         h_member[heneeds] << i 
         p h_member
         h_count[heneeds] += 1
      end
     #=>    a[heneeds] << i  if heneeds <= n 
}
allin=true

"1".upto(n.to_s).each {|index|
   if h_count[index] > index.to_i or h_count[index] < 1
      next
   elsif h_count[index] == index.to_i
      allin=false
      h_member[index].each {|member|  print "#{member} "}
   else # h_count[index] < index.to_i
      
   end
   
}
if allin == true
   print "1\n #{n} "
   1.upto(n).each {|mem| print "#{mem} "}
end
# 
# 1.upto(n-1).each {|i|
#    temp = a[i].select {|x| !x.nil?} ; len = temp.count
#    
#     if len  == i
#        print "#{i} "
#        temp.each {|o| print "#{o}  "}
#        puts
#     elsif  len == 0 
#        next
#     elsif len < i
#         
#        print "#{i} "
#        temp.each {|o| print "#{o} "}
#        imple = a[i-len]
#        imple.each {|o| print "#{o} "}
#        puts 
#     end
# }

# 
# wishes.each_with_index {|e,i|
#    if e.to_i <= n
#       h[e] << (i+1)
#    end 
# }
# 
# p h 



=begin
# 1.upto(n).each {|i|
#    a[i] = Array.new(i,[])
# }
# a[2] << 3
p a 

# h = Hash[(Array 1..n).map(&:to_s).zip(Array.new(n,[]))]
# which_needs = Array.new(n) {Array.new(n,0)}
$order = 0 ; wishes= []
=end