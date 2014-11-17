# 1800 Murphy's Law


=begin
var w,g,h,l,t:real;
begin
g:=981;
read(l,h,w);
if l/2>h then begin write('butter'); halt end;
t:=sqrt(2*(h-l/2)/g);
w:=frac(w*t/60);
if ((w>=0) and (w<=1/4)) or ((w>=3/4) and (w<=1)) then write('butter') else write('bread');
end.
=end