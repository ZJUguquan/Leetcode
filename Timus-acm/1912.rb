#acm 1712 
a=[
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]
]
b=[
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]
]
i=1
while i <=4
   line = gets.chomp!
   str = line.scan(/./) 
   str.each_with_index do|c,index|
      a[i-1][index] = c.to_s   
   end
   i +=1
end
i = 1
while i <=4
   line = gets.chomp!
   str = line.scan(/./) 
   str.each_with_index do|c,index|
      b[i-1][index] = c.to_s   
   end
   i +=1
end

# p a
# p b

0.upto(3).each{|i|
   0.upto(3).each { |j|
      if a[i][j] != "."
         print b[i][j]
      end
   }  
}
a1 = a.transpose.map &:reverse
0.upto(3).each{|i|
   0.upto(3).each { |j|
      if a1[i][j] != "."
         print b[i][j]
      end
   }  
}
a2 = a1.transpose.map &:reverse
0.upto(3).each{|i|
   0.upto(3).each { |j|
      if a2[i][j] != "."
         print b[i][j]
      end
   }  
}

a3 = a2.transpose.map &:reverse
0.upto(3).each{|i|
   0.upto(3).each { |j|
      if a3[i][j] != "."
         print b[i][j]
      end
   }  
}




# print 



   # 
# string.each_with_index {|c,index|
#    a[0][index] =  c.to_s
# }
# p a