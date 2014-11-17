# 1796 amusement park
numbers = gets.chomp!.split(" ").map {|x| x= x.to_i}
price = gets.chomp!.to_f  # one ticket < 1000
#numbers = [ 0,2,0,0,0,0]; price = 10
def amount(numbers)
   numbers[0]*10+numbers[1]*50+numbers[2]*100+numbers[3]*500 +numbers[4]*1000+numbers[5]*5000
end

total = amount(numbers) 
tic_1 = (total/price ).to_i
numbers_reduce= numbers
numbers.each_with_index {|e,i|
    if e > 0
       numbers_reduce[i] = numbers[i]-1
       break
    end 
    
}
#p numbers_reduce 
total_reduce = amount(numbers)
tic_2 = (total_reduce / price).to_i + 1
#p tic_1 ;p tic_2
puts  (tic_1-tic_2+1)
tic_2.upto(tic_1).each {|i| print "#{i} " }

