
s = gets.chomp!
output = [] ; 
n = s.length ; k = 1; s1= s[0]

while true  # k: leftpoint  len : rightpoint 
   i= 1
             while  n - i >= k+i  and s[n-i] == s[k+i]
                i += 1
             end
   if n-i <= k+i
        print (s+s1)
      break
   end
   
   s1 = s[k] +s1
   k += 1 
end


=begin
my idea for solution
  k := 2;
  n := length(s);
  s1 := s[1];
  while true do begin
    i := 0;
    while (n - i >= k + i) and (s[k + i] = s[n - i]) do inc(i);
    if n - i <= k + i
    then begin
      write(s + s1);
      halt;
    end;
    s1 := s[k] + s1;
    inc(k);
  end;
# class String
#   def remove(index)
#     self[0..(index-1)] + self[(index+1) ..self.length ]
#   end
#   def is_Palindrome?
#      s = self
#      while s.length > 1 and s[0] == s[s.length-1]
#         s = s[1..s.length-2]
#      end
#      if s.length <=1
#         return true
#      else 
#         return false
#      end
# end
=end

# # 1354 
# class String
#   def remove(index)
#     self[0..(index-1)] + self[(index+1) ..self.length ]
#   end
#   def is_Palindrome?
#      s = self
#      while s.length > 1 and s[0] == s[s.length-1]
#         s = s[1..s.length-2]
#      end
#      if s.length <=1
#         return true
#      else 
#         return false
#      end
# end
# 
# class Stack
#   def initialize
#     @array = []
#   end
# 
#   def push val
#     @array.push val
#   end
# 
#   def pop 
#     @array.pop
#   end
# end
# 
# s = "OnLine"; 
# st= Stack.new 
# s.each_char {|c| st.push(c)}
# 
# p s.is_Palindrome?
# # 
# # def is_Palindrome?(s)
# #    while s.first == s.last
# #       s = s[1..s.length-2]
# #    end
# #    if s.length <=1
# #       return true
# #    else 
# #       return false
# #    end
# # end
# # 
# # n=s1.length ; k = 2
# # s1 = s[0] ;
# # while true 
# #    i = 0; 
# #    while ( n- i >= k + i) and (s[k+i-1]= s[n-i]) 
# #       i += 1
# #    end
# #    if n-i <= k+i
# #       print (s+s1)
# #    end
# #    s1 = s[k-1] +s1
# #    k += 1
# # end
# # 
# # 
# #  s_r = s1.reverse
# # resIn= s1 << s_r ; resIn = resIn.remove(len)
# # 
# # 
# # p resIn
# 
# 
# # 
# # def makepl(s)
# #    len=s1.length / 2 ; 
# #    while (s[len-1] == s[len])
# #       s = s[0..len-2] + s[(len+1)..(s.length-1)]
# #       len = s.length/2
# #  