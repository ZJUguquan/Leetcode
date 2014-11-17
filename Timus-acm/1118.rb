# 1118 Nontrivial Numbers 
i,j = gets.chomp!.split(" ").map(&:to_i)

if i == 1
   puts 1
elsif i == j 
   puts i
else
   deyer = [] ; idx = 0;  min = 10000;  mineded = 0
   j.downto(i).each {|ii|
      (ii/2).downto(1).each {|jj|
         if(ii % jj ==0)
            if jj < min 
               min = jj
               mineded = ii
               if (jj==1)
                  puts ii
                  next
               end
            end
            break
         end
      }
   }
   puts mineded
end

=begin

def triviality(n)
   sum = 0
   1.upto(n-1) {|i| sum +=i if n % i == 0 }
   return sum/n.to_f
end

 #res = i #arr = Array.new(j-i + 2, 0)
h = {}
i.upto(j).each {|e| h[e] = triviality(e)}

puts h.key(h.values.min)


=end

=begin

import java.util.Scanner;
public class problem1197 {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int I = in.nextInt();
        int J = in.nextInt();

        if (I == 1) {
            System.out.println(1);
            return;
        }
        if (I == J) {
            System.out.println(I);
            return;
        }
        int deyer[] = new int[100001];
        int idx = 0;
        int min = 10000;
        int mineded = 0;

        for (int i = J; i >= I; i--) {

            for (int j = i / 2; j >= 1; j--) {

                if (i % j == 0) {
                    if (j < min) {
                        min = j;
                        mineded = i;
                        if (j == 1) {
                            System.out.println(i);
                            return;
                        }
                    }

                    break;
                }
            }
        }
        System.out.println(mineded);

    }
}
=end