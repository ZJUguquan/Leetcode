
sca =  0.70710678118654752440084436210485
s = gets.chomp! #{}"13412349082103941290"

x,y= 0,0
# p s
final_x ,final_y = 0,0 
s.each_char {|c|

when 1
  x -= sca; y -= sca
when 2
  y -= 1
when 3 
  x += sca; y -= sca
when 4 
  x -= 1
when 6  
  x += 1
when 7 
  x-= sca ; y += sca
when 8 
  y += 1
when 9
  x += sca ; y += sca
when 0
  final_x, final_y = x,y
  break
else
end
}

final_x = x
final_y = y 

printf "%.10f %.10f",final_x,final_y
