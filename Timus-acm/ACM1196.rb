# ACM 1196
# n=["1054","1492"]
# a=[1492,65536,1492,100].map {|e| e.to_s}
# b=a.each_with_object(Hash.new(0)) { |o, h| h[o] += 1 }
# p b
 
n=gets.chomp.to_i
st=[]
1.upto(n).each {
  in1 = gets.chomp.to_i
   st << in1 
 }
pro = []
m = gets.chomp.to_i
1.upto(m).each {
  in2 = gets.chomp.to_i
   pro << in2 
 } 
b = pro.each_with_object(Hash.new(0)) {|o,h|  h[o] += 1}
output = 0 
st.each  { |e| 
   output += b[e] if pro.include? e
}
puts output