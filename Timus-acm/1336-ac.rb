# 1336

 arr = []; n = gets.chomp!.to_i
 1.upto(n).each do |s|
    arr << temp=gets.chomp!
 end
 puts n-arr.uniq.length 