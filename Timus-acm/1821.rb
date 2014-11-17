# 1821

n= gets.chomp!.to_i ; real_time = [] ;  h ={:best => 0} ; counter = 0 ; counter_order = 1; 
bestpeople = [] 
name1, time1 = gets.chomp!.split(" ")
mins1, seconds1 = time1.split(":").map(&:to_f)
real_time << mins1 * 60 + seconds1
counter = 1 ; h[:best] = real_time[0]; bestpeople << name1
if n == 1
   puts 1
   puts name1

else # n >= 2
   2.upto(n).each {|i|
      name, time = gets.chomp!.split(" ")
      mins, seconds = time.split(":").map(&:to_f)
      real_time << ti =( mins * 60 + seconds + (i-1) * 30)
      if ti - (i-counter_order)* 30 < h[:best]
         counter += 1 ; counter_order = i
         h[:best] = ti
         bestpeople << name
      end
      h[name] = ti
   }

   puts counter ; 
   bestpeople = bestpeople.sort
   bestpeople.each {|o| puts o}
end



# 6
# Zaitseva 21:38.2
# Hauswald 21:21.0
# Boulygina 22:04.4
# Henkel 22:06.1
# Wilhelm 21:11.1
# Jonsson 22:05.8