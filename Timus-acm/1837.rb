#1837 # 0: spec 1: teammate 2: teammatemate 3 :undefined
n=gets.chomp!.to_i
h = {} ; arr = Array.new(Array.new)
teammates= [] ;spec = "I"
teammatemates=[]; other = []
total = [] 
h[spec] = 0
1.upto(n).each do |i|
   arr[i] = gets.chomp!.split(" ")
   total << arr
   teammates =  teammates +  (arr-[spec]) if arr[i].include?(spec)
end
teammates = (teammates.flatten - [spec,nil] ).uniq ; arr = arr-[nil]
total = (total.flatten-[nil]).uniq.sort
   
# there is no In-
   if !total.include? (spec)
      h = Hash[total.zip(Array.new(total.length,"undefined"))]
      h.each {|k,v| puts "#{k} #{v}" }
# have >=1 In- 
   else
      arr.each_with_index do |element,index|
         # find teammate 's teammates
         # if have teammate 's teammate
               if !(temp = element - [element, teammates ].inject(&:&) ).empty?
                  teammatemates <<  temp
               end
      end
       h = Hash[total.zip(Array.new(total.length,"-1"))]
       h.keys.each { |k|
          if k == spec
             puts "#{k} 0"
          else
            puts "#{k} 1" if teammates.include?(k) 
            puts "#{k} 2" if teammatemates.include?(k) 
            puts "#{k} undefined" if !teammatemates.include?(k) and !teammates.include?(k)
         end
       }
   end
   




# 
# 
# 
# 1.upto(n).each do |j|
#    # check spec
#    if arr[j-1].include (spec)
#    
#    
#    arr[j].each { |ele|
#     h[ele] = -1 if !h.has_key?(ele)   
#     if teamates.include (e)
#       h[ele] = 1
#          
#    }
# end
# p teammates  
# p arr

=begin
   if [arr[i]
   teammatemates + (arr-)
=end
