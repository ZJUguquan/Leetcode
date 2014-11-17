#1685

@s = "orthography"
@arr = [] ;  @i = 0

def recurse (low, high)
   if low > high
      return
   end
   
   mid = (low + high)/2
   @arr << mid
   # print  @@s[@@i]
 #   @@i +=1
   recurse(low,mid-1)
   recurse(mid+1,high)
end

recurse(0, @s.size-1)

@arr.each {|i| print @s[i]}