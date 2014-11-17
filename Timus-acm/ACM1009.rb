# 1009 

tokens = []
while string = gets do
   string.split().each do |token|
      tokens << token
  end
end

@nDigit = tokens[0].to_i
@kBased = tokens[1].to_i

@ans = Array.new(18 )
@ans[1] = @kBased - 1
@ans[2] = @kBased * ( @kBased - 1)

if  @nDigit ==2 
  puts  @ans[2]
else
  for i in 3.. @nDigit do 
    @ans[i] = (@kBased - 1) *(@ans[i-1]+@ans[i-2])
  end
end

puts @ans[@nDigit]
