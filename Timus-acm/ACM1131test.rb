#  acm 1131: copying
#  read  n, k


#n, k = gets.chomp.split(" ").collect {|x| x.to_i}
$used_hours = 0 

n=8 ; k=3
if n ==1
  $used_hours = 0 
elsif n == 2
  $used_hours =1

elsif n == 3
  $used_hours = 2
else  # n >= 4
  if k == 1
    $used_hours = n-1
  else #if k >= 2
      $used_hours = Math.log2(k).floor + 1
      data_computer = 2**$used_hours

      if data_computer < n 
        if k > n 
          $used_hours += 1
        else
                while  data_computer < n 
                  data_computer += k 
                  $used_hours += 1
                end
        end
      end
  end
end 


puts $used_hours



  