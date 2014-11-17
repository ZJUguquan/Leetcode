
var name:array [1..300]of string;
    i,j:longint;
    n,k:longint;
    s:string;
    str:string;
    x,y,z:longint;
    a:array [1..300,1..300]of longint;
    v,u:array [1..300]of longint;
    w:longint;
    p:boolean;
function add(s:string):longint;
var i:longint;
    t:boolean;
begin
  t:=false;
  for i:=1 to k do
    if s=name[i] then
    begin
      t:=true;
      break;
    end;
  if t then add:=i else
  begin
    inc(k);
    name[k]:=s;
    add:=k;
  end;
end;


begin
  k:=0;
  readln(n);
  for i:=1 to n do
  begin
    readln(s);
    if s[length(s)]<>' ' then s:=s+' ';
    str:=copy(s,1,Pos(' ',s)-1);
    delete(s,1,Pos(' ',s));
    x:=add(str);
    str:=copy(s,1,Pos(' ',s)-1);
    delete(s,1,Pos(' ',s));
    y:=add(str);
    str:=copy(s,1,Pos(' ',s)-1);
    z:=add(str);
    a[x,y]:=1;
    a[y,z]:=1;
    a[x,z]:=1;
    a[y,x]:=1;
    a[z,y]:=1;
    a[z,x]:=1;
  end;

  for i:=1 to k do
    v[i]:=-1;
  z:=k;
  x:=add('Isenbaev');
  if k=z then
  begin
    v[x]:=0;
    p:=true;
    w:=0;
    while p do
    begin
     p:=false;
     for i:=1 to k do
       if v[i]=w then
         for j:=1 to k do
           if (a[i,j]=1)and(v[j]=-1) then
           begin
             v[j]:=w+1;
             p:=true;
           end;
     inc(w);
    end;
  end else dec(k);
  for i:=1 to k do u[i]:=i;

  for i:=1 to k-1 do
    for j:=1 to k-i do
      if (name[u[j]]>name[u[j+1]]) then
      begin
        x:=u[j];
        u[j]:=u[j+1];
        u[j+1]:=x;
      end;
  for i:=1 to k do
  begin
    write(name[u[i]],' ');
    if v[u[i]]=-1 then writeln('undefined') else writeln(v[u[i]]);
  end;
end.
	
	
	var
	 mass,have:array[0..400] of string;
	 mark:array[0..400] of integer;
	 go,p,n,i,l,k,j:longint;
	 g,ex:string;
	 iska,find:boolean;
	begin
	 readln(n); iska:=false;
	 for i:=1 to n do
	  begin
	   readln(g); mass[i]:=g+' ';
	   if pos('Isenbaev ',mass[i])<>0 then iska:=true;
	  end;
	 i:=1; inc(l);have[l]:='Isenbaev ';mark[l]:=0;
	 while i<=l do begin
	  for j:=1 to n do
	   begin
	    if pos(have[i],mass[j])=0 then continue;
	    while mass[j]<>'' do
	     begin
	      k:=pos(' ',mass[j]);
	      ex:=copy(mass[j],1,k); find:=false;
	      for p:=1 to l do
	       if ex=have[p] then find:=true;
	      if not find then
	       begin
	        inc(l); have[l]:=ex; mark[l]:=mark[i]+1;
	       end;
	      delete(mass[j],1,k);
	     end; end;
	    inc(i);
	   end;
	 for i:=1 to n do
	  while mass[i]<>'' do
	   begin
	    k:=pos(' ',mass[i]);
	    ex:=copy(mass[i],1,k); find:=false;
	    for p:=1 to l do
	     if ex=have[p] then find:=true;
	    if not find then
	     begin
	      inc(l); have[l]:=ex; mark[l]:=-1;
	     end;
	    delete(mass[i],1,k);
	   end;
	 if not iska then
	  begin
	   have[1]:=have[l];
	   mark[1]:=mark[l];
	   dec(l);
	  end;
	 for i:=l downto 2 do
	  for j:=1 to i-1 do
	   if have[i]<have[j] then
	    begin
	     ex:=have[i];have[i]:=have[j];have[j]:=ex;
	     p:=mark[i];mark[i]:=mark[j];mark[j]:=p;
	    end;
	 for i:=1 to l do
	  if mark[i]>-1 then writeln(have[i],mark[i])
	                else writeln(have[i],'undefined');
	end.
	