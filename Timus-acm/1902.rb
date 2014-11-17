# 1902 Neo-Venice
d=[];out=[];n,time,start = gets.chomp!.split(" ").map {|x| x=x.to_i}
s = gets.chomp!.split(" ").map {|x| x=x.to_i }
s.each{|e|  out <<  (e+time-start)/2.0}
out.each_with_index {|o,i| printf "%3.6f\n", o+start}


