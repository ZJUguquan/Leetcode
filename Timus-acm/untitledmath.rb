# # ACMP 1011 Conductors
# 
# # input p q 
# # 0.01 <= p  q<=99 
# # p more than p %  conductors
# # q less than q % conductors
# 
# 
# 
# #p = gets.chomp.to_f
# #q = gets.chomp.to_f
# 
# p = 13.0 / 100
# q= 14.1 /100
# 
# p = p.rationalize
# q = q.rationalize
# 
# p_d = p.denominator
# p_n = p.numerator
# q_d = q.denominator
# q_n = q.denominator
# 
# 
puts FLOAT::EPSILON
puts FLOAT:MIN
# 
# max = [p_d, q_d].max  
# $ouput = Array.new(1000)
# 
# 
# for every_deno in 3 .. 100
#   for every_numer in 1.. (every_deno-1)
#      value = every_numer.to_f / every_deno.to_f
#      if value >= p and value <= q  
#          puts "minimal ren:#{every_deno}"        
#      end
#   end
# end
#        
#   
# 
# 
# puts $output[0]
# 
# 
# #puts p + q 
