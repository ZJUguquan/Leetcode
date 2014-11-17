# ACM 1084
include Math
len, r = gets.chomp.split(" ").collect {|x| x.to_i}
len=len.to_f 
r = r.to_f
if r <= len / 2.0
  puts (Math::PI * r* r).round(3) 
else
  if  r >= Math.sqrt(2) * len / 2 
    puts (len * len).round(3.0)
  else
    # arc area 
    # 
    pi = Math::PI
    circlearea = pi*r*r
   # puts "circle: #{circlearea}"
    az = 2*Math.acos(len/2/r) 
#   puts "az: #{az}"
    s = pi*r*r *az/2/pi# shan shape area

    b = 2*Math.sqrt(r*r-len*len/4)  
    stru = len/4*b   
    s = s-stru
    s= pi*r*r -4*s
    puts s.round(3)


  end
end






    # fanarea = (1-4*Math.acos(len/r/2)/2/Math::PI)*r*r*Math::PI
    # tri_area = len*Math.sqrt(r*r-(len*len)/4)
    # arglearea = fanarea - tri_area  
    # total= Math::PI*r*r
    # puts (total-4*arglearea).round(4)
    # #(Math::PI*r*r-4*Math.acos(len/r/2) *r*r+2*len*Math.sqrt(r*r - len*len/4 ) ).round(3)
  