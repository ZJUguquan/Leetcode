# 1881 Long problem statement

h,w,n = gets.chomp!.split(" ").map {|x| x.to_i }

curso=-1; usedLines = 0

1.upto(n).each do |s|
   # iterate  every word.   
   s = gets.chomp!
   len = s.length   
  # the curso  ,  there are some types:
  # empty line ,  curso = -1   
    if curso == -1 
       usedLines += 1
       curso += 1 + len  #(begin with new line)
    else   # this line  (temp)
          curso += 1 + len    # think about it   can hold or go to next line
      
    
       if curso == w
          curso = -1
       end
    
       if curso > w 
          curso = len
          usedLines += 1
       end
    end
 end

 #p usedLines

pages = usedLines / h
pages += 1 if usedLines % h > 0
puts pages    
       
       
 #