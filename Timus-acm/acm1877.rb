#acm 1877


a=gets.chomp!
b=gets.chomp!

t=[]
"0000".upto("9999").each{|e|
    t << e 
}

p1=t.index(a) + 1
p2=t.index(b) + 1


if p1 % 2 == 1  or p2 %2 ==0
    puts "yes"
else 
    puts "no"
end

# 2121
# 7878

# 3232
# # odd odd
# "yes"
# # odd even



# # even even 
# puts "yes" 


# puts "yes" if "0002" > "0001"

# puts "no" if "000"  
# #n = gets.chomp.to_i
