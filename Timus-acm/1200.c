#include <stdio.h>
main()
{
  double p1,p2;
  int n,m1,m2,zs;
  scanf("%lf%lf", &p1, &p2);
  scanf("%d",&n);
  if (p1 < 0) p1=0;
  if (p2 < 0) p2=0;
  zs=floor(p1/2);
  m1=(p1 /2 - zs) > 0.5 ? zs+1:zs;
  zs=floor(p2/2);
  m2=(p2 /2 - zs) > 0.5 ? zs+1:zs;
  if (n < (m1+m2))
  {
    double temp;
    temp=(p1-p2+2*n)/4;
    zs=floor(temp);
    m1= ((temp- zs) > 0.5) ? zs+1:zs;
    if (m1 < 0) m1=0;
    if (m1 > n) m1=n;
    m2=n-m1;
  }
  printf("%.2f\n",((m1*p1) + (m2*p2) - m1*m1 -m2*m2));
  printf("%d %d\n",m1,m2);
  return 0;
}
