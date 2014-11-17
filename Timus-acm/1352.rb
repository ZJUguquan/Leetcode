# 1352 Mersenne Primes 

def hor(n)
case n
when 1
   res = 2
when 2
   res =3 
when 3
   res = 5
when 4
   res = 7
when 5
   res = 13
when 6
   res = 17
when 7
   res = 19
when 8
   res = 31
when 9
   res = 61
when 10
   res = 89
when 11
   res = 107
when 12
   res = 127
when 13
   res = 521
when 14
   res = 607
when 15
   res = 1279
when 16
   res = 2203
when 17
   res = 2281
when 18
   res = 3217
when 19
   res = 4253
when 20
   res = 4423
when 21
   res = 9689
when 22
   res = 9941
when 23
   res = 11213
when 24
   res = 19937
when 25
   res = 21701
when 26
   res = 23209
when 27
   res = 44497
when 28
   res = 86243
when 29
   res = 110503
when 30
   res = 132049
when 31
   res = 216091
when 32
   res = 756839
when 33
   res = 859433
when 34
   res = 1257787
when 35
   res = 1398269
when 36
   res = 2976221
when 37
   res = 3021377
when 38
   res = 6972593
else
   return res
end

end

n = gets.chomp!.to_i ; int = []; out = []
1.upto(n).each {|index| int << gets.chomp!.to_i 
   out << hor(int.last)
}
out.each {|o| puts o}


=begin   
   1	 2	 1	 1	----	----	 
   2	 3	 1	 2	----	----	 
   3	 5	 2	 3	----	----	 
   4	 7	 3	 4	----	----	 
   5	 13	 4	 8	 1456	 anonymous	 
   6	 17	 6	 10	 1588	 Cataldi	 
   7	 19	 6	 12	 1588	 Cataldi	 
   8	31	 10	 19	 1772	 Euler	 
   9	61	 19	 37	 1883	 Pervushin	 
   10	 89	 27	 54	 1911	 Powers	 
   11	 107	 33	 65	 1914	 Powers	note
   12	 127	 39	 77	 1876	 Lucas	 
   13	 521	 157	 314	 1952	 Robinson	 
   14	 607	 183	 366	 1952	 Robinson	 
   15	 1279	 386	 770	 1952	 Robinson	 
   16	 2203	 664	 1327	 1952	 Robinson	 
   17	 2281	 687	 1373	 1952	 Robinson	 
   18	 3217	 969	 1937	 1957	 Riesel	 
   19	 4253	 1281	 2561	 1961	 Hurwitz	 
   20	 4423	 1332	 2663	 1961	 Hurwitz	 
   21	 9689	 2917	 5834	 1963	Gillies	 
   22	 9941	 2993	 5985	 1963	 Gillies	 
   23	 11213	 3376	 6751	 1963	 Gillies	 
   24	 19937	 6002	 12003	 1971	 Tuckerman	[Tuckerman71]
   25	 21701	 6533	 13066	 1978	Noll & Nickel	[NN80]
   26	 23209	 6987	 13973	 1979	 Noll	"
   27	 44497	 13395	 26790	 1979	 Nelson & Slowinski	[Slowinski79]
   28	 86243	 25962	 51924	 1982	 Slowinski	[Ewing83]
   29	 110503	 33265	 66530	 1988	 Colquitt & Welsh	[CW91]
   30	 132049	 39751	 79502	 1983	 Slowinski	 
   31	 216091	 65050	 130100	 1985	 Slowinski	 
   32	 756839	 227832	 455663	 1992	 Slowinski & Gage et al.	(web page)
   33	 859433	 258716	 517430	 1994	 Slowinski & Gage	 
   34	 1257787	 378632	 757263	 1996	 Slowinski & Gage	(web page)
   35	 1398269	 420921	 841842	 1996	Armengaud, Woltman, 
   et al. (GIMPS)	(web page)
   36	 2976221	 895932	1791864	 1997	Spence, Woltman,
   et al. (GIMPS)	(web page)
   37	 3021377	 909526	1819050	 1998	Clarkson, Woltman, Kurowski
   et al. (GIMPS, PrimeNet)	(web page)
   38	 6972593	
=end