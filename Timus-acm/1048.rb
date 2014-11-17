# 1048 superlong sums

n = gets.chomp!.to_i
 a =[]; b = []
1.upto(n).each { |s|
   left, right = gets.chomp!.split(" ").map(&:to_i)
   a << left ; b << right 
}
a = a.reverse; b = b.reverse 
c = Array.new(n+1,0)
0.upto(n-1).each {|index|
   t = a[index] + b[index] 
   if t  < 10 
      c[index] += t 
   else
      c[index] += t - 10
      c[index+1] += 1
   end 
   
}
#p c
(n-1).downto(0).each {|e| print c[e]}

# if c.last == 0
#    (n-1).downto(0).each {|e| print c[e]}
# else
#    (n).downto(0).each {|e| print c[e]}

#include <cstdio>
#include <cstdlib>



int main()
{
     char str[8];
     gets (str);
     int n=atoi(str);

    char s,sum=0;

    int count=0;

    while (n)
    {
        gets(str);

        s=str[0]+str[2];

        if (s==105) {putchar(57); --n;}
        else {sum=s; --n; break; }
    }

    if (!n) return 0;


    for (int i=0; i<n; ++i)
    {
        gets(str);

        s=str[0]+str[2];


        if (s==105) {++count;}
        else
        {


            if (s<=104)
            {

                putchar(sum-48);

                for (; count>0; --count)
                    putchar(57);

                sum=s;

            }
            else
            {

                if (s>=106)
                {

                    putchar(sum-47);

                    for (; count>0; --count)
                    putchar(48);

                sum=s-10;

                }
            }
        }


    }

    if (s==105)
    {

            putchar(sum-48);

        for (; count>0; --count)
                putchar(57);

    }
    else
        if (sum)

            (s>=106)?putchar(s-58):putchar(s-48);
}
# end