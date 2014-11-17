#  1869 

$n = gets.chomp!.to_i ; matri = Array.new($n) {Array.new($n,0)}
1.upto($n).each {|row|
   matri[row-1] = gets.chomp!.split(" ").map(&:to_i)
}
# # count  from 
people_come = 0; people_go = 0 

def count_from_up(ma, i) # station : i  A->B count people at i station  
   sum = 0 ; (i).upto($n-1).each { |k| sum += ma[i-1][k] }
   return sum
end

def count_from_down(ma, i) # station : i  count people   down i ( up before i)   array: i-1
   sum = 0;(i-2).downto(0).each { |k| sum += ma[k][i-1] }
   return sum
end

def count_back_up(ma, i) # station : i   cong i shang . 
   sum = 0;(i-2).downto(0).each { |k| sum += ma[i-1][k] }
   return sum
end

def count_back_down(ma, i) # station : i 
   sum = 0;($n-1).downto(i).each { |k| sum += ma[k][i-1] }
   return sum
end


curr_people_cnt =  0 

0.upto($n-1).each  {|k| 
   curr_people_cnt +=  (count_from_up(matri,k) - count_from_down(matri,k))
}

p curr_people_cnt
# 1.upto($n).each {|k|
#    print "#{k} #{count_from_up(matri,k) }"; 
#    # print "#{k} #{count_from_down(matri,k) }"; 
# }

# 

# 

#    
# 
# 

# 1.upto($n-1).each {|k|
#    #people_come +=
#     p (count_from_up(matri,k) -   count_from_down(matri,k))
#    #people_go  += 
#    #(count_back_up(matri,k) - count_back_up(matri,k))
# }
# 
# p people_come
# p people_go

# count to
