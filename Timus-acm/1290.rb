# 1290  Sabotage
# input 4 1 6  output:  3 2 2 2 1 1
# >=0, >=1
input = []  ;n = gets.chomp!.to_i;
if n == 0
   puts
else
    1.upto(n).each {input << temp=gets.chomp!.to_i}
    input.sort.reverse.each {|e| puts e}
end





=begin
    0.upto(input.max-1).each do |i|   
          step2 <<  input.count {|x| x > i}
       end
    0.upto(step2.max-1).each do |i|   
          puts  step2.count {|x| x > i}
    end
=end