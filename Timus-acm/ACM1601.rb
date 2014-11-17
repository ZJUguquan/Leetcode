# 1601  
# 
# 
# 
# 
i = 0
 STDIN.read.each_char {|c|
    if(i==0&&c>='A'&&c<='Z')
        print c 
        i = 1
    else
        if(c>='A' and c<='Z')
             print c.downcase
         else
            print c
        end
   end
  i=0  if(c=='.'||c=='!'||c=='?')

}
 
# input = STDIN.read
# input3=input.downcase.split()
# for i in 1.. (input.length-1)
#    input3[i].upcase if input3[i-1].to_s <="a"  and !input3[i].nil?
# end
# print input[0]
# 1.upto(input.length-1).each {|i| print input3[i] }






# stringline = "HOW DID YOU I AM A BLONDE?"
# shou = stringline[0]
# newline = ""
# stringline.each_char {|c|
 
# }

# # puts stringline



# a='A'

# b= a.downcase

# puts b 
