# ACM 1319 
# include Matrix
require 'matrix'  # bundled with Ruby
n = 3
#result = [][]
result = [[3,4],[4,3]]

# p result
# m = Matrix.zero(n)
# m[1][1] = 1.5
# p m 
=begin
  k:=0;
      p:=n-1;
      for s:=1 to (n*2-1) do begin
                                  for i:=1 to n do for j:=1 to n do if j-i=p then begin
                                                                                       k:=k+1;
                                                                                       a[i,j]:=k
                                                                                  end;
                                  p:=p-1
                              end;

=end


# m = Matrix[
#  [1, 2, 3],
#  [4, 5, 6]
# ]
=begin
  
if n == 1
    return 1
  else  # n > = 2 
  k = 0
  p = n - 1


    s = 0 
    while s <= (2*n -1)  
            for i in 0 .. (n -1 )  do 
                for j in 0 .. (n-1 )  do 
                                          if j - i == p  
                                            #   右上角 
                                                            k += 1
                                                            ans[i][j] = k
                                          end

                                          
                 end

            end
    p -= 1     
    s += 1
    end
        #  
  end

  #include<iostream.h>
int  i,j;
long a[101][101],n;
 int main(){
    cin>>n;
   for(i=1;i<n+1;i++)
 {   a[i][n]=i*(i+1)/2;
  }
   for(i=1;i<n;i++)
 {  for(j=n-1;j>=i;j--)
  {  a[i][j]=a[i][j+1]+n-j+i-1;
   }
 }
   for(i=2;i<n+1;i++)
 {  for(j=i-1;j>0;j--)
  {  a[i][j]=a[i][j+1]+n+j-i;
   }
 }
   for(i=1;i<n+1;i++)
 { for(j=1;j<n+1;j++)
    cout<<a[i][j]<<" ";
    cout<<"\n";
  }
 return 0;
}
=end


