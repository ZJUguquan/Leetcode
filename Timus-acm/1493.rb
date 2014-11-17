#1493 
n = gets.chomp!.each_char.to_a.map {|x| x=x.to_i }
s1 = n[0]+n[1] +n[2] ; s2 = n[3]+n[4]+n[5]
d = s1 - s2
if  n[5]>0 and n[5] <9 
      puts "Yes"
elsif n[5] == 9
   if d == -1 
      puts "Yes"
   else
      puts "No"
   end
else
# n [5] = 0 
   if d==1
      puts "Yes"
   else
      puts "No"
   end
end 
      
      
      # 715 068,  小大  后-1 可减
      # 445 219   大小  后不能+ 
      # 012 200   大小  后面是0
   
