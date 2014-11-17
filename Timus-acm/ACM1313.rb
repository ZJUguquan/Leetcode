# ACM 1313
n = gets.chomp!
n = n.to_i

i = 0
ans = Array.new(n + 1){Array.new(n + 1)}
while i < n 
  temp = gets.chomp!
  temp_chars = Array.new(n + 1)
  temp_chars = temp.split.to_a 
   j = 0 
   while j < n 
    ans[i][j] = temp_chars[j]
    j += 1
    end
    i +=1
  end


$result = []
sum = 0 
   while sum <= (2 * n -2)
          for j in 0.. (n-1)
             for i in 0 ..(n-1)
                if i + j == sum
                     $result << ans[i][j]
                      end
                   end
             end
    sum += 1
  end
$result.each {|x| print x+" "}  

