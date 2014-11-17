i, fi, j ,fj, n  = gets.chomp!.split(" ").map(&:to_i)
t = 0
if i > j
   i,j  =j,i ; fi,fj = fj,fi
end
d=j-i
a = Array.new(4001,0) ;f = Array.new(2001,0) ;  
f[1]= 1 ;f[2] = 1   
3.upto(d).each { |k| f[k] = f[k-1]+ f[k-2] }


b = ( ( fj - f[d-1] *fi)/f[d] ).floor   # F(i+1)
 
    a[i]= fi ; a[i+1] = b; 
#p [i,fi,j,fj,n ,d,b]; p f.select {|x| x > 0} ; 

    if n > i
       (i+2).upto(n).each {|k| a[k] = a[k-1]+a[k-2]  }
    else # n < i
       (i-1).downto(n).each {|k| a[k] = a[k+2] - a[k+1]  }
    end

 puts a[n]
    
    
