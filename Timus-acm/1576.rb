# 1576 telephone tariffs
n1,c1 = gets.chomp!.split(" ").map(&:to_i)# [135,1]
n2,t,c2 = gets.chomp!.split(" ").map(&:to_i) #[220,10,1]
n3 = gets.chomp!.to_i # 300
talk_minutes = 0 
k = gets.chomp!.to_i
1.upto(k) do |e|
   s = gets.chomp!
   mi = s[0,2].to_i ; se = s[3,2].to_i
   if  mi == 0 and se < 7 
      next
   end
   mi += 1 if se != 0 
   talk_minutes += mi
      
end

p talk_minutes
unlimited = n3
combined =  talk_minutes > t ? n2 + c2*(talk_minutes-t) : n2
basic = n1 + talk_minutes * c1
# Basic:     155
# Combined:  230
# Unlimited: 300
printf "Basic:     %d\n",basic
printf "Combined:  %d\n",combined
printf "Unlimited: %d\n",unlimited
#print "Basic:\t\t#{fee1}\nCombined:\t#{fee2}\nUnlimited:\t#{fee3}"

=begin
Basic:     16
Combined:  102
Unlimited: 1000
Basic:     16
Combined:  102
Unlimited: 1000
uses
  SysUtils;
var i,n,n1,n2,n3,c1,c2,t,t1,t2,sum:longint;
s:string;
//a:array [1..1001] of longint;
begin
 read(n1,c1);
 read(n2,t,c2);
 read(n3);
 readln(n);
 sum:=0;
 for i:=1 to n do
  begin
   readln(s);
   t1:=strtoint(copy(s,1,2));
   t2:=strtoint(copy(s,4,2));
   if (t1=0) and (t2<6) then sum:=sum+0 else
     if (t2>0) then sum:=sum+t1+1 else sum:=sum+t1;
  end;
 writeln('Basic:     ',n1+c1*sum);
 if sum<=t then writeln('Combined:  ',n2) else writeln('Combined:  ',n2+(sum-t)*c2);
 write('Unlimited: ',n3);
end.
=end