#1102 
def pickout(s)
   return s.gsub(/output|out|puton|input|in|one/,"")
end
output = [] 
n = gets.chomp!.to_i
1.upto(n).each {|k|
   line = gets.chomp!
   output << pickout(line)
}
output.each {|el|
   puts el == "" ? "YES" : "NO" 
}







