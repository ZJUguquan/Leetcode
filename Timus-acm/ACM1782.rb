# 1782 turn 

a, b = gets.chomp!.split(" ").collect {|i| i.to_i }
c = []
c_all = gets.chomp!.split(" ").collect {|i| i.to_i }
s = 0 
1.upto(b) do |i|
   c = c_all[i-1]
   s +=  c - a 
   s = s < 0 ? 0 : s
end
   
puts s
   
   
   
=begin
var a,b,c,d,i:integer;
begin
read(a,b);
d:=0;
for i:=1 to b do
begin
read(c);
if d<0 then d:=0;
d:=d-(a-c);
end;
if d > 0 then writeln (d) else writeln ('0');
end.
   
=end
         