#1102 
$a=[];$b=[]
$a[1]="out"; $a[2]="output"; $a[3] = "puton"
$b[1]="in";  $b[2]="input";  $b[3]="one"

def pickout(s,what)
   return s.gsub(what,"")
end

def picka(s)
   s = pickout(s,$a[2])
   s = pickout(s,$a[3])
   s = pickout(s,$a[1])
   s
end
def pickb(s)
   s = pickout(s,$b[2])
   s = pickout(s,$b[3])
   s = pickout(s,$b[1])
   s
end
input = [] ; output = [] 
n = gets.chomp!.to_i
1.upto(n).each {|k|
   input << line = gets.chomp!
}

input.each {|el| 
   el =  picka(el)
   output << el =  pickb(el)   
}

output.each {|el|
   puts el == "" ? "YES" : "NO" 
}