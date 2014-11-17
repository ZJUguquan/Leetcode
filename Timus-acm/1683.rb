# # 1683 fridge
a=0; k =[]
n = gets.chomp!.to_i ; m=0;
while n >= 2
   m += 1 ;   n = n - (n >> 1)
   k[m] = n
end
puts m
1.upto(m).each {|e| print "#{k[e]} "}



# # n = gets.chomp!.to_i
# # if n == 1 
# #    print "0\n0"
# # elsif n ==2
# #    print"1\n\1"
# # else   # n >2
# #    temp = n/2
# #    while (n-temp) > 0
# #       print "#{temp} "
# #       n = temp; temp = n/2
# #    end
# # end
# 
# 
# 
# def ououput(n)
#    if n == 1 
#       return 1 
#    else     
#       res = n - n/2
# 
#          while res > 2
#             puts n/2   
#             n= res
#             res = n - n/2
#             if res == 1
#                puts 1
#                els res ==2
#                puts "1"
#             end
#             
#       end
#    end
# end
# 
# ououput(15)