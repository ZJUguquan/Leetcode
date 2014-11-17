
# n digits
# k-based

n =  gets.chomp.to_i
k = gets.chomp.to_i  

res = 0
def solu(n,k)
   if k == 2
      if n == 2 
         res = 2
      elsif n == 3 
         res = 2 + 1
      else  # n>= 4
         res = solu(n-1,2) + solu(n-2,2) 
      end
   else # k >=3 
      if n == 2
         res = k*(k-1)
      elsif n == 3
         res = (k-1)*k*(k-1)+(k-1)*1*(k-1)
      else
         res = (k-1)*(solu(n-1,k) + solu(n-2,k) )
      end

   end
end

puts solu(n,k)

=begin
import java.math.BigInteger;
import java.util.Scanner;

public class bigKnum {

    public static void main(String args[]){
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int k=in.nextInt();

        BigInteger f1,f2,f3;
        f1=BigInteger.valueOf(k-1);
        f2=f1.multiply(BigInteger.valueOf(k));

        for(int i=2;i<n;i++)
        {
            f3=(f1.add(f2)).multiply(BigInteger.valueOf(k-1));
            f1=f2;
            f2=f3;

        }
        System.out.print(f2);

    }

}
=end