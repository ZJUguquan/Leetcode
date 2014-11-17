# acm 1149 

n = gets.chomp.to_i

def outputOperator(n, k)
    print "sin(#{k}"
    if k < n
      if k % 2 == 0 
        print "+"
      else
        print "-"
      end
      outputOperator(n, k+1)
    end
    print ")"
end

def outputNumber(n, k)
  if k < n 
    print "("
    outputNumber(n, k+1)
    print ")"
  end
  outputOperator(n - k + 1 , 1)
  print "+#{k}"

end

outputNumber(n,1)














=begin
  
I thought i'll never get AC at this problem, but after some time i wrote that very nice (as for me ^___^) functions doing the work.

void a( int n, int k )
{
-printf("sin(%d",k);
-if ( k < n )
-{
--if ( k % 2 )
---printf("-");
--else
---printf("+");
--a( n, k + 1 );
-}
-printf(")");
}

void s( int n, int k )
{
-if ( k < n )
-{
--printf("(");
--s( n, k + 1 );
--printf(")");
-}
-a( n - k + 1, 1 );
-printf("+%d",k);
}

For answer just need to call s( n, 1 ).
Good luck!

Edited by author 20.03.2010 18:23
  
=end