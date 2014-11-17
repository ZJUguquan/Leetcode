
s = gets.chomp!
#s = "AbabaAab" # AbabaAab abA
n = s.length ; k = 1; s1= s[0]
while true  # k: leftpoint  len : rightpoint 
   i= 0 ; 
             while  n-1-i >= k+i  and s[n-i-1] == s[k+i]
                i += 1
             end
   if n-i-1 <= k+i
      print (s+s1)
      break
   end
   s1 = s[k] +s1
   k += 1 
end
  