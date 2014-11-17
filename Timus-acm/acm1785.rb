#acm 1785




n = gets.chomp.to_i

def check(n)
   return "few" if n>=1 and n<5
   return "several" if n>=5 and n < 10
   return "pack"  if n>=10 and n<20
   return "lots" if n>=20 and n <50
   return "horde" if n>=50 and n<100
   return "throng" if n>=100 and n< 250
   return "swarm" if n>=250 and n<500
   return "zounds" if n>=500 and n<1000
   return "legion" if n>=1000
end
puts check(n)  