# ACM 1263 elections
# 
# len, r = gets.chomp.split(" ").collect {|x| x.to_i}
n, m=gets.chomp.split(" ").collect {|x| x.to_i}
vv = Array.new(m+1,0)
i = 1
while i <= m
	vote = gets.chomp.to_i
	vv << vote
	i += 1
end
#p vv
#b = pro.each_with_object(Hash.new(0)) {|o,h|  h[o] += 1}
count = vv.each_with_object(Hash.new(0)) {|o,h| h[o] += 1}
sum = 0

1.upto(n).each {|i|  sum += count[i]}
percent=[]
1.upto(n).each {|i|  
   percent << (count[i].to_f / sum.to_f  * 100 ).round(2)
}
percent.each {|p| 
  if p >0
    puts "%5.2f%" % p
 else
      puts "%5.2f%" % 0
   end
}

