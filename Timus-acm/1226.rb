# 1226

input = ""

output =[] ; 
input = STDIN.read.split("\n").each { |line|
   newline = []

   line.split(" ").each {|q|
      newline << q.gsub(/\w+/) { |match| match.reverse }
   }
   output << newline
}

p output 

output.each {|ele|
   ele.each {|elesub|  print "#{elesub} "  }   
   puts
}


=begin
      if elesub[0] == "," or elesub[0] == "." or elesub[0] == "?" or elesub[0] == "!"
         b = elesub.each_char.to_a.rotate(1)
         b.each {|index| print index}
      else
         print "#{elesub} " 
      end}
=end