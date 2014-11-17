# 1112. Cover 
# max number 
# unintersect  interval 

n = 5

class Interval
   attr_accessor :left
   attr_accessor :right
   def initalize()
   end
end

# 
#    
# interval = Array.new(3000){-2}
# # 1.upto.n {|e|
# #    interval << gets.chomp!.split(" ").map(&:to_i)
# # }
# h = {}
# 1.upto(n).each {|e| 
#    arr = gets.chomp!.split(" ").map(&:to_i)
#    left= arr.min ; right = arr.max
#    interval[left] = 0; interval[right] = 2 if interval[left] + interval[right]== -4 
#    if interval[right] == 2
#       
#    elsif interval[right] = 0
#          
#       
#    h[right+e*0.01] = [left,right]
# }
# 
# h  = h.sort.reverse
# 
# points = Array.new(1000){0}
# curr_max = h.keys.max.floor 
# points[curr_max] = 1
# h.each {|k,v| # v[0] left v[1] right
#    
#    if k.floor = curr_max 
#       curr_min =  h.select {h.keys}
# 
# } 
# p points
# 
# 
# #p h.values
# h.each 
# 
# h = {} 
# 
# def inbao(a,b)
#    if b[0]>= a[0] and b[1]<= a[1]
#       return 1 # b <= a    use  
#    elsif  b[0] <= a[0] and b[1]  >= a[1]  
#       return  -1    #  
#    elsif  b[1] <= a[0]  or b[0] >= a[1]  # no common, excep a point
#       return 5
#    else  # intersect half
#       return 0
#    end
# end
#        
#       
# p interval