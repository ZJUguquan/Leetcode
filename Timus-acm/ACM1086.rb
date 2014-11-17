# acm 1086 cryptography

n = gets.chomp!
n = n.to_i

def is_prime?(n)
  if n <= 1 
    return false
  elsif n ==2
    return true
  else
    if n % 2 ==0 
      return false
    else
      i = 3
      while (i * i <= n)
        if n%i ==0 
          return false
        end 
        i += 2
      end
      return true
    end
  end
end


all = []
all[0]=1
for i in 1..163853
  if is_prime?(i)
    all << i 
  end
end

times = 1
where = []
while times <= n
  co = gets.chomp!
  co = co.to_i
  where << co
  times += 1
end
where.each{|x| 
  puts all[x]
}

# 1.upto(20000000) {|e|
#  if  is.prime?(e) then
#      all << e
#  end
# }


# puts "d "

# puts all.length
# puts all[15001]

# if n <= 1
#   puts 0
# else 





