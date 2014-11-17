a = Array.new(100000,0)
b = Array.new(10,0) 
a[1]=1  ;  a[0]=0

for k in 2..100000 
	if k % 2 == 0 
		a[k]=a[k/2]
	else
		a[k]=a[k/2] +a[k/2+1]
	end
end



k = 0
while true
	n = gets.chomp.to_i
	if n == 0 
		break
	else
		
		b[k] = n
    k = k+1
	end
end

n = k -1
for k in 0.. n 
	max = 0
	s=b[k]
	for j in 1.. s
		if a[j] > max then max = a[j] 
		end
	end
	puts max 
end


# for i in 2..99999 {|i|
# 	max = a[i-1]



#   if e % 2 == 0
#     a[e] = a[e / 2]
#   else
#     a[e] =a[ e/2] + a[e/2 + 1]
#   end
# }

