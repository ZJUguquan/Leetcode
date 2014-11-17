# 1572 

def maxLength(t,a)
   case t
   when 1
      return 2 * a
   when 2
      return Math.sqrt(2) * a
   when 3
      return a
   else
      puts "not this type"
   end
end


def minLength(t,a)
   case t
   when 1
      return 2 * a
   when 2
      return  a
   when 3
      return a * Math.sqrt(3) / 2
   else
      puts "not this type"
   end
end

t, a = gets.chomp!.split(" ").map(&:to_i)    # [1, 5 ]
arr=[];  count = 0
n = gets.chomp!.to_i ; 1.upto(n).each {|i| 
    intype, ina = gets.chomp!.split(" ").map(&:to_i)   
   count += 1 if maxLength(t,a) >= minLength(intype,ina)
}
puts count
   
   