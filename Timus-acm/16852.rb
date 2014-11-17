#1685

@s = "Vasya likes soup."
@n = @s.length
k = @n ;  a=Array.new (20005) 
b=Array.new(20005)
@s.each {|ind|
    a << ind
}
@arr = [] ;  @i = 0 ; @left = 1; @right = @n 
listR = []; listO= []

orta = (@left + @right) /2


1.upto(@n).each {|i|
  puts "L=#{@left} R=#{@right} O=#{orta}"
  b[orta] = a[i]   if @left <= @right 
  if @left < @right
    listR << (@right)
    @right = orta - 1
    listO << orta
    orta = (@left + @right) /2
  else
    p listO
    @left = listO.size
}





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
p @s.length
p @arr
@arr.each {|i| print @s[i]}