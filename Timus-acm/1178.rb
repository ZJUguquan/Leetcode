# 1178  Akbardin's roads 
n = 4

a1 = [0,2]  ; a2= [1,1] ; a3=[3,4] ; a4= [4,4]


 
 
var a:array[1..10000]of longint;
    b:array[1..10000]of integer;
    q,l,r,j,i,x,n:longint;
procedure Qsort(l,r:integer);
begin
     if l>=r then exit;
     j:=r;i:=l;x:=a[i];
     while not(i=j) do begin
           while (a[j]>x)and(j>i) do dec(j);
           if i<j then begin q:=a[i];a[i]:=a[j];a[j]:=q;
                             q:=b[i];b[i]:=b[j];b[j]:=q;inc(i);end;
           while (a[i]<x)and(j>i) do inc(i);
           if i<j then begin q:=a[j];a[j]:=a[i];a[i]:=q;
                             q:=b[i];b[i]:=b[j];b[j]:=q;j:=j-1;end;
           end;
     x:=a[i];
     if l<(i-1) then Qsort(l,i-1);
     if (i+1)<r then Qsort(i+1,r);
end;
begin
     read(n);
     for i:=1 to n do readln(a[i]);
     for i:=1 to n do b[i]:=i;
     Qsort(1,n);
     for i:=1 to n div 2 do writeln(b[2*i-1],' ',b[2*i]);
     readln;
end.