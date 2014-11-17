# 1640   circle and radius
n = gets.chomp!.to_i ;  points = Array.new(n) { Array.new(2) {}} 
distance =[] # distance beween orgin and points 0 -  N-1


if n ==1 
    x,y = gets.chomp!.split(" ").map(&:to_i)
    r = 2.012034011 ; diff= 0.011
    print "#{x+diff} #{y-diff} #{r}"


else
   1.upto(n).each {|i| 
      x,y = gets.chomp!.split(" ").map(&:to_i)
      points[i-1] = [x,y]
      distance << Math.sqrt(x*x+y*y)
   }

   # d_index = distance.index(distance.max) 
   r = [distance.sort[n-2] - 0.0000001, 999].min
   print "0 0 #{r}"

end


=begin
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
#define maxn 105
const double eps = 1e-9;
double x[maxn],y[maxn],cx,cy,r;
int main()
{
    int n;
    scanf("%d",&n);
    for(int i = 0;i < n;i++)
        scanf("%lf %lf",&x[i],&y[i]);
    cx = cy = 0.1;
    r = 0.0;
    for(int i = 0;i < n;i++)
        r = max(r,sqrt((cx - x[i]) * (cx - x[i]) + (cy - y[i]) * (cy - y[i])));
    printf("%.10lf %.10lf %.10lf\n",cx,cy,r);
}
=end