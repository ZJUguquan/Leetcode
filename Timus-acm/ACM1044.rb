
# ACM 1044  lucky tickets 

# n = gets.chomp!
# n = n.to_i 
# 
Sum = Array.new(37,0) 
"0000".upto("9999").each {|e|
	temp = 0
	e.each_char { |c|
      temp += c.to_f
	}
	Sum[temp] += 1
}
total = 0
puts Sum.map { |e| total += e*e}


if n == 2
  return 10 
elsif n ==4
  return 670
elsif n == 6
   
  return  55252
else # n== 8

  return 4816030 
end
    

n=gets.chomp.to_i

case n
 when 2
   puts 10 
when 4
  puts 670
when 6
  puts 55252
when 8
  puts 4816030
end     