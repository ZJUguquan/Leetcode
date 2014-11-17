#  1224 spiral

n, m=gets.chomp.split(" ").collect {|x| x.to_i}

def turns(n,m)
  case n 
  when 1 
    return 0
  when 2
    case m 
    when 1  
      return 1
    else
     return 2
    end
  else
    case m 
      when 1  
        return 1
      when 2
         return 3  
      else
        return turns(n-2, m-1)+4
    end
  end
end


puts turns(n,m)
     # puts turns(3**10,2**12)






=begin
  
var m,n,y:real;b:boolean;
begin
 readln(m,n);
 b:=false;
 if m>n then begin y:=m;m:=n;n:=y;b:=true end;
 if m=0 then begin writeln(0);halt;end;
 if frac(m/2)<>0 then y:=int(m/2)*4
  else y:=int((m-1)/2)*4+2;
 if b then writeln(y+1:0:0) else writeln(y:0:0);
end.
  
end
  = 