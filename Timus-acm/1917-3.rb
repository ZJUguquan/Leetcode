
if n == 1
   if a[0] <= p 
      print "1 1"
   else
      print "0 0"
   end
else
   ko_magic_cnt = 0 ;  ko_coins_cnt = 0
   used_magic_cnt=0 ; damaged_coins_cnt = 0
   a.uniq.each_with_index {|e,i|
      total_damage = damage(a,e)
      if total_damage > p # dead
         next
      else
         ko_coins_cnt = cnt_n(a,e)} 
         ko_magic_cnt=1
      end
      
   }
   
end
