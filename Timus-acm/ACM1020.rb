
# acm 

total = gets.chomp!
a,b = total.split(" ")
a= a.to_i
b= b.to_f
times = 1
totalp =[]

while times <= a 
  temp = gets.chomp!
  p = []
  p[0],p[1] = temp.split(" ")
  p[0]= p[0].to_f
  p[1]= p[1].to_f
  totalp << p
  times += 1
end

def eudi(p1,p2)
  a1=p1[0].to_f
  a2=p1[1].to_f
  b1=p2[0].to_f
  b2=p2[1].to_f
  if a1 ==nil then a1=0 end
    if a2 ==nil then a2=0 end
      if b1 ==nil then b1=0 end
        if b2 ==nil then b2=0 end

return Math.sqrt(  (a1-b1)**2 + (a2-b2)**2 ) 
end

R = b
total1= 2 * R * Math::PI
sum =0
for i in (-1)..(a-2)
 sum += eudi(totalp[i], totalp[i+1])
end
To = total1+ sum  



puts To.round(2)

#puts a 
#puts b
=begin
   
 rescue Exception => e
   
 end
  
#  return Math.sqrt( (p1[0].to_f-p2[0]) * (p1[0]-p2[0]) + (p1[1]-p2[1]) * (p1[1]-p2[1]) )
=end
  