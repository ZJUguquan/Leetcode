# 1931 excellent team 
n = gets.chomp!.to_i
a = gets.chomp!.split(" ").map(&:to_i)
count = Array.new(n,0)
min = a[0] ; max = 0 ; j = 0; maxn = 0 

1.upto(n-1).each do |i|
   
end

=begin
#include<stdio.h>
#define N 100005
int a;
int main()
{
	int n,i,j,num,temp,min,maxn;
	while(scanf("%d",&n)!=EOF)
	{
		scanf("%d",&a);
		min=a;
		j=0;
		num=0;
		maxn=0;
		temp=0;
		for(i=1;i<n;i++)
		{
			scanf("%d",&a);
			num++;
			if(a<min)
			{
				if(num>maxn)
				{
					maxn=num;
					temp=j;
				}
				min=a;
				j=i;
				num=1;
			}
		}
		if(num>maxn)temp=j;
		printf("%d\n",temp+1);
	}
	return 0;
}
=end



# 
# 0.upto(n-2).each {|i|
#    j = i + 1
#    if a[i] > a[j]
#       count[i] += 1
#       a[i] <=> a[j]
#    end
#    while ( a[i] < a[j] )
#       if j < n-1
#          j += 1
#          count[i] += 1
#       else
#          break
#       end
#    end
# }
#       
# p count 
#    
#    
#  #   
#    while (a[i] < a[j])
#       j += 1
#       if (j-i >= s)
#          if max > 0 
#             s = j-i +1
#          else 
#             s = j - i 
#             max = i
#          end
#       end
#    end
# }
# print max+1