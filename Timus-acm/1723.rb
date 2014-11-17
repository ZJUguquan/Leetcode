# 1723
#=> 返回两个字符串中最长子串 
def subsequence(s1, s2)
 
        return 0 if s1.empty? || s2.empty?
 
        num=Array.new(s1.size){Array.new(s2.size)}
        s1.scan(/./).each_with_index{|letter1,i|
            s2.scan(/./).each_with_index{|letter2,j|
 
                    if s1[i]==s2[j]
                        if i==0||j==0
                           num[i][j] = 1
                        else
                           num[i][j]  = 1 + num[i - 1][ j - 1]
                        end
                    else
                        if i==0 && j==0
                           num[i][j] = 0
                        elsif i==0 &&  j!=0  #First ith element
                           num[i][j] = [0,  num[i][j - 1]].max
                        elsif j==0 && i!=0  #First jth element
                            num[i][j] = [0, num[i - 1][j]].max
                        elsif i != 0 && j!= 0
                          num[i][j] = [num[i - 1][j], num[i][j - 1]].max
                        end
                    end
            }
        }
        num[s1.length - 1][s2.length - 1]
 
end
 
puts subsequence("houseboat","computer")
# 
# def find_longest_at_2_substring(s1,s2) 
#    # s1 parent string  s2 substring
#    # s2 belongs s1
#    m = 0 
#    



# 
# def self.find_longest_common_substring(s1, s2)
#   if (s1 == "" || s2 == "")
#     return ""
#   end
#   m = Array.new(s1.length){ [0] * s2.length }
#   longest_length, longest_end_pos = 0,0
#   (0 .. s1.length - 1).each do |x|
#     (0 .. s2.length - 1).each do |y|
#       if s1[x] == s2[y]
#         m[x][y] = 1
#         if (x > 0 && y > 0)
#           m[x][y] += m[x-1][y-1]
#         end
#         if m[x][y] > longest_length
#           longest_length = m[x][y]
#           longest_end_pos = x
#         end
#       end
#     end
#   end
#   return s1[longest_end_pos - longest_length + 1 .. longest_end_pos]
# end
# 
# 
# 
# 
# p find_longest_common_substring("abcdef","abcef")#=>
# 

