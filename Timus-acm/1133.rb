# 1133 Fibonacci sequence
 i, Fi, j ,Fj, n  = gets.chomp!.split(" ").map(&:to_i)
 if i > j then i<-> j; Fi <- Fj; end
 f = Array.new(2001,0) ; f[1] = 1; f[2]= 1; 
 a = Array.new(4002,0)
 if j-i > 3
    3.upto(j-i).each {|l| f[l] = f[l-1]+f[l-2] }
    b = ((Fj - Fi * f[j-i-1] )/(f[j-i])).floor
    a[i] = Fi ; a[i+1]= b 
    
    

# def feb(i,j,n) # i ! = j 
#    diff = (i-j).abs
#    if i > j 
#       
#    else # i < j 
#       
#    end
# end
def fibo(n)
   if n==1 or n == 2 
      1
   else
      return fibo(n-1) + fibo(n-2)
   end
end
farr = []
1.upto(2000).each {|i| farr << fibo(i) }
=begin
fi 
fj = f1 + f2 


fi =F2 fn-1 + F1fn-2 = F3fn-2 + F2fn-3 = 3fn-3 + F3fn-4 = 5 fn-4 + 3fn-5
=   F(i-j+1) fj +  F(F(i-j)fj-1
   i-k + 1=j  
= Fn f1 + F(n-1) f0   
   
fi = ii;   =  Fi.f1 + F(i-1) f0
fj = jj;   =  Fj.f1 + F(j-1) f0

fn = nn    =  Fn.

    
program t1133;
var a1,a2,i1,j1,n,j,i,t1:longint;
    b,x1,y1,t:extended;
    f:array[0..2000]of extended;
    a:array[-2000..2000]of extended;
begin
     readln(i1,x1,j1,y1,n);
     if i1>j1 then begin t1:=i1; i1:=j1; j1:=t1; t:=x1; x1:=y1;
y1:=t; end;
     f[1]:=1; f[2]:=1;
     for i:=3 to j1-i1 do f[i]:=f[i-1]+f[i-2];
     b:=trunc((y1-x1*f[j1-i1-1])/(f[j1-i1]));
     a[i1]:=x1; a[i1+1]:=b;
     if n>i1 then
        for i:=i1+2 to n do
            a[i]:=a[i-1]+a[i-2];
     if n<i1 then
        for i:=i1-1 downto n do
            a[i]:=a[i+2]-a[i+1];
     writeln(a[n]:0:0);
end.
   
   
=end