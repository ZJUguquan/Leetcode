# 1917 titan ruins 
n, p =  gets.chomp!.split(" ").map(&:to_i)  #[5,4]
arr = gets.chomp!.split(" ").map(&:to_i).sort  #[4,1,4,1,2]
h = Hash.new ;arr.uniq.each {|e| h[e] = arr.count(e)}
h.each_pair {|k,v| h[k] = k * v  }
a =[] ;   count = 0 
used_magic = 0 
class Array
  def cumulative_sum
    sum = 0
    return self.map{|x| sum += x}
  end
end
dama_mu = h.values.cumulative_sum
h_mu = Hash[h.keys.zip(dama_mu)]

h_um = h_mu.invert

maxhurt = (h_mu.values.sort.select {|x| x < p } ).last
#p "not exceed p, max damage #{maxhurt}"

firstshot= h_mu.key(maxhurt)
#p "not exceed p, max point #{h_mu.key(maxhurt)}"
used_magic = 1; count = arr.count{|x| x<= firstshot}

# output more than  first shot 
shots = [] ; shots << firstshot

arr.uniq.select { |x| x>firstshot}.sort.each {|trythis|
   if h[trythis] < p
      used_magic += 1
      shots << trythis
      count += arr.count(trythis)
      break
   end

} 
# p h
# p h_mu
# p shots
print "#{count} #{used_magic}"
# 
# secondshort = (arr.select {|x| x > firstshot}).sort.first
# 
# p secondshort
# if  h[secondshort] < p
#    used_magic += 1
#    count += arr.count(secondshort)
# end


=begin
9 10
4 1 4 1 2 3 2 3 4

=end


# maxd = arr.max ;  poss = Array.new(maxd+1,0)
# 

# def damage(arr,n)   # 当发射n时 对自己的总伤害
#    return (arr.select {|x| x <=n }).inject(:+)
# end
# 
# def cnt_n(arr,n)   # 当发射n时   打掉的coins 数目
#    return arr.select {|x| x<= n}
# end
# 
# if n > 1 

# 
#    used_magic = 0 ; damage_coins_cnt = 0 
#    accum_damage = 0  ; ko1= 0 ; ko_cnt=0
#    hurt_to_big=[] ; damage_coins_this_time =[] ; index = -1
#    h.keys.sort.each {|h_key| 
#       hurt_acc ={} ; h[0]= 0
#       if h[h_key] <= p
#          index += 1
#          used_magic += 1 
#          hurt_to_big << h[h_key]
#          damage_coins_this_time << h[h_key]/h_key
#          damage_coins_cnt += h[h_key]/h_key
#       end
#    
#    
#      hurt_to_big
# #    p damage_coins_this_time   
#    #print  "#{damage_coins_cnt} #{used_magic}" 
#    }
#    hurt_accum=hurt_to_big.cumulative_sum
#    
#    # (index).downto(1).each {|d|
# #       if hurt_accum[index] <=p
# #          ko1= 1; ko_cnt=
# #    }
# 
# else
#    if arr[0] <= p
#       print "1 1"
#    else
#       print "0 0"
#    end
# end


