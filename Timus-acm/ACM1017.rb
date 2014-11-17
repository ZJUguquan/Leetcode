# ACM 1017
def add(a,b)
   if  a==nil and b==nil
      return 0
   elsif a ==nil and b!= nil
      return b
   elsif b == nil and a!=nil
      return a
   else
      return a + b
   end
end

      
n = gets.chomp!
n = n.to_i
ans = Array.new(n + 1) {Array.new(32)}
for i in 1..n
   ans[i][1] = 1
end


if n ==5
  puts 2
elsif n ==6
  puts 3
elsif n ==7 
  puts 4
elsif n ==8
  puts 5
else  
  ans[4][2]=1
ans[5][2]=1
ans[6][2]=2
ans[6][3]=1
ans[7][2]=3
ans[7][3]=1
ans[8][2]=3
ans[8][3]=2
for i in 9.. n
   for j in 1..32
       ans[i][j] = add( ans[i- j ][j - 1] , ans[i - j][j])
    end
 end


 $methods_count = 0
    for j in 1..32
       $methods_count = add($methods_count, ans[n][j]) 
    end
    $methods_count -= 1
 puts $methods_count
end




=begin
  
F[i][j]=F[i-j-1][j+1]+F[i][j+1];
cout << F[N-1][0]-1<< endl;;
 
d[i][j] = d[i-j][j-1](if the 1st step only have one brick) + d[i-j][j]
(if the 1st step have more than one brick).

=end


