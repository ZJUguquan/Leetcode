# ACM1100 Final Standings 
# 
n = gets.chomp.to_i
team = {}
1.upto(n).each { |i|
   line = gets.chomp
   id,solved = line.split(" ").collect {|x| x.to_i} 
   team[i] = solved

}

v_sorted = team.values.sort.reverse

v_sorted.each{ |v|
   puts "#{team.key(v)} #{v}"  
}





# p team.keys
# p team.values




# team.each{ |k,v| 
#   puts "k:#{k} v:#{v}" 

# }
