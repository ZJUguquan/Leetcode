#1917new 
class Array
  def cumulative_sum
    sum = 0
    return self.map{|x| sum += x}
  end
end

$n, $p = gets.chomp!.split(" ").map(&:to_i) #[11,7]
a = gets.chomp!.split(" ").map(&:to_i)   # [1,1,1,2,1,1,1,3,4,4,5]

$magic_count  = 0 ; $coins_cnt = 0
def count_element(a)
   h = {} ; au = a.uniq.sort
   au.each {|e|    h[e] = a.count(e)  * e}
   h
end

def recurshot(a,p) 
   while  !a.empty? and a.min < p 
      uni_a = a.uniq.sort ;  h = count_element(a)
      #a.uniq.sort.each {|e| h[e] =  e * (a.count(e)) }
      dama_mu = h.values.cumulative_sum
      
      h_mu = Hash[h.keys.zip(dama_mu)]
      curr_shot = h_mu.key((h_mu.values.sort.select {|x| x < p }).last)
      if curr_shot.nil?
         break
      else
          # puts "now a: #{a}"
#           puts "now h: #{h}"
#           puts "this time: curr_shot #{curr_shot}"
         $magic_count += 1 ; 
         $coins_cnt += a.count {|x| x <= curr_shot}
         a = a.delete_if {|x| x <= curr_shot}    
      end
   end
end


if $n == 1
   if a[0] > $p
      print "0 0"
   else 
      print "1 1"
   end
else
   recurshot(a,$p)
   print "#{$coins_cnt} #{$magic_count}"
end
   
       

=begin
11 7
1 1 1 1 2 1 1 3 4 4 5
# ans 8 2
=end
