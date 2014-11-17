# ACMP 1011 Conductors

# input p q 
# 0.01 <= p  q<=99 
# p more than p %  conductors
# q less than q % conductors



#p = gets.chomp.to_f
#q = gets.chomp.to_f

p = 13 / 100
q= 14.1 /100


i = 2 
while (true)
  min = (i * p).round
  max = (i * q).round
  C = max.floor
  if  C > min and C < max and C >=1
    break
  end
  i++
end

def rrd( d)
  return ((d*10000+0.5)/10000 ).floor
end


p = p.rationalize
q = q.rationalize

p_d = p.denominator
p_n = p.numerator
q_d = q.denominator
q_n = q.denominator


max = [p_d, q_d].max  
$ouput = []
3.upto(max).each { |every_deno|
  1.upto(max-1).each{ |every_numer|
     value = every_numer / every_deno
     if value >= p and value <= q
       $output << every_deno
     end
       
  }
}


puts $output[0]


#puts p + q 
