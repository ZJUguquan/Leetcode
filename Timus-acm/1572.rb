# 1572  Great well

t, a = gets.chomp!.split(" ").map(&:to_i)    # [1, 5 ]
arr=[]; n = gets.chomp!.to_i ; 1.upto(n).each {|i| 
   arr << temp = gets.chomp!.split(" ").map(&:to_i)   } 

# 
# arr << [2,10]
# arr << [1,6]
# arr << [2,11]
# arr << [2,11]

def canyouin?(type,a,typein, ain)
   if type == typein 
      if type == 1   # circle 
         return true if ain <= a 
         return false if ain > a
      elsif type == 3
         if a >= ain * Math.sqrt(3)/2
            return true
         else
            return false
         end 
      else 
         if  a * Math.sqrt(2)  >= ain 
            return true
         else 
            return false
         end  
      end
   else  
      case type
      when 1 # circle
         if typein == 2
            return true if a * 2>= ain 
            return false if  a *2 < ain 
         else
            # typein == 3
            return true if a *2 >= ain * Math.sqrt(3)/2
            return false if  a *2 < ain * Math.sqrt(3)/2
         end
      when 2 # square 
         if typein == 1  # circle in 
            return true if a *Math.sqrt(2) >= ain * 2
            return false if a*Math.sqrt(2) < ain * 2  # a < ain * Math.sqrt(2)
         else
            # typein == 3 # tri 
            return true if  a *Math.sqrt(2) >= ain * Math.sqrt(3)/2
            return false if a *Math.sqrt(2) < ain * Math.sqrt(3)/2 #   < ain * Math.sqrt(3)/2
         end
      
      
      
      
      else # 3
         if typein == 1
            return true if a * Math.sqrt(3)/2 >= ain * 2
            return false if   a * Math.sqrt(3)/2 < ain * 2
         else
            # typein == 2
            return true if a * Math.sqrt(3)/2 >= ain
            return false if  a * Math.sqrt(3)/2 < ain
         end
      end
   end
end
count = 0
arr.each_with_index {|e,index|
   if canyouin?(t,a,e[0],e[1])
      count += 1 
     # puts "#{index+1} can in "
   end
}
puts count 