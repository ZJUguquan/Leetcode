# 1864 
n = gets.chomp!.to_i
a = []; 
a = gets.chomp!.split(" ").map(&:to_i) 
if n == 1 
   puts 100
else
   
asum = a.inject(:+) ; 
aaver = asum /(n+1+0.00000000001) 
getter = a.count {|x| x > aaver}
aget = a.select {|x|  x > aaver} ; 
agetsum = aget.inject(:+);
agetaver =  agetsum/(getter.to_f)
aget2 = [] ; 
aget.each{|e| aget2 << e - aaver }
total = aget2.inject(:+)



pay = Array.new(n,0) ; t = 100.0
1.upto(getter).each {|e|
   pay[e-1] = ( ( (aget2[e-1]/total.to_f) +0.0001)* t).floor
}

pay.each {|e| print "#{e} "
 } 
end


=begin

/*
 * ACM Timus Online Judge Contest 15 October 2011
 * Problem C - Get-Together at Den's
 */

#include <cstdio>

int N;
double A[100];

int main()
{
#ifndef ONLINE_JUDGE
        freopen("input.txt", "rt", stdin);
#endif
        int i;
        double sum, med = 0;

        scanf("%d", &N);
        for (i = 0; i < N; i++)
        {
                scanf("%lf", &A[i]);
                med += A[i];
        }

        med /= (double) (N + 1);

        for (i = 0; i < N; i++)
        {
                A[i] -= med;
        };

        sum = 0;
        for (i = 0; i < N; i++)
                if (A[i] > 0)
                {
                        sum += A[i];
                }

        for (i = 0; i < N; i++)
                if (A[i] > 0)
                {
                        printf("%d ", (int)(A[i] * 100 / sum + 0.000001));
                }
                else
                {
                        printf("0 ");
                }

        return 0;
}

=end