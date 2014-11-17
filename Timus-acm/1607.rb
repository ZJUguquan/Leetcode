# 1607 
# Taxi

a,b,c,d = gets.chomp!.split(" ").map {|x| x.to_i}
e =  ( (c=[a,c].max) -a)  /(b+d)
puts ( a+=(e+1)*b ) < (c -= e* d) ? a : c




#a max , c 0 -> c
#c max      c = 850 / 150  = 5  e = turns
   
   
   
# 150 50   1000 100
# 200  900 
# 250  800 
#300 700 
#350  600 
#400 500 

#450 