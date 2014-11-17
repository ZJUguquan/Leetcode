# 1139

n,m = gets.chomp!.split(" ").map {|x| x.to_i}
n = n - 1
m = m - 1
a = n.gcd(m)
res = a *(n/a + m/a -1)
#res2 = n + m - a
puts res