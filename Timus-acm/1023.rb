# 1023 buttons


k = gets.chomp!.to_i

if k % 3 == 0
  puts 2
elsif k % 4 == 0
  puts 3
else
  r = 4
  while (k % (r+1)  != 0) 
    if (r+1)*(r+1) > k 
      print "#{k-1}"
      return  0
    end
    r += 1
  end
  puts (r-1)
end

=begin
var i,k:longint;
begin
 read(k);
 i:=k div 3;
 while(k mod i<>0) do
   i:=k div(k div i +1);
write(k div i-1);
end.

=end



# if k >= 3
#   puts "#{k-1}"
# end

