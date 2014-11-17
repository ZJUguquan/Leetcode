# 1213 cockroaches
rooms = [] ; counter = 0
STDIN.each_line {|line|
   line = line.chomp!
   if line == "#"
      break
   end
   if line.include? "-"
      a,b = line.split("-")
      rooms << a ; rooms <<b
   else
      rooms  << line
      
   end
}

p rooms.uniq.length-1
