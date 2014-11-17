# 1025 Democracy in Danger 
# 
#  Accepted 

tokens = []
while string = gets do
   string.split(/\D/).each do |token|
      tokens << token.to_i
  end
end

@n = tokens[0] #  group number 
i = 1 
@Groups= []
while (i < tokens.size) do 
  if tokens[i] > 0 
    @Groups << tokens[i].to_i
  end
  i += 1
end

@Groups = @Groups.sort

half = @Groups.size / 2  + 1 

result = 0
i = 0 
while(i < half)  
  result += @Groups[i] / 2 + 1 
  i += 1 

end

p result


# puts @Groups[0]

# puts @Groups.sort

# puts @n


# @GroupCount.each  { |e| 
#   @Groups << e.to_i
# }
  

 # every gorup count 

# @GroupCount = @GroupCount.sort
