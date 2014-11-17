# 1142 relations,   several numbers relation.   count. 

def factorial(n)
   if n== 0 or n == 1 
      return 1
   else
      return (1..n).inject(:*)
   end
end

def combinator(n,m)
   if n==m or m==0
      return 1
   else
         return factorial(n)/(factorial(m) *(factorial(n-m)))
      end
end

def cut(n,k) # k >=2  
   if k == 1 
      return 1
   else
      res = combinator(n-1, k-1)
      res =  res.even? ? res/2 : res/2 +1
   end
   return res
end
      

def f_c(n,k)  # n number count ;  k : groups
   if k == 1  
      return 1
   elsif k == 2
      
      
      
       factorial(n)
   else
      return factorial(k) * (combinator(n,k) )
   end
end  
   
def howm(n)
   i = 1; sum = 0
   while i <= n
      sum += f_c(n,k) ; i += 1
   end
   sum 
end
       
         
   if n == 2 
      return  1 + 2*1 
   elsif n == 3
      return  1 + c(3,2)* 2! + 3!
   else
      return 1 +  