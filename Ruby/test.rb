
# remember: everything is objects
# single line comment
p 3.class # Fixnum

p 3.to_s  # "3"

p '*' * 40

# Simple Hanghang(5age) calculator

p 1 + 2
p 5 - 3
p 4 * 2
p 4 / 2

p '*' * 40

# compare

p 3 > 1
p 3 >= 3
p 2 < 2

p '*' * 40

# true false and nil
p nil
p nil.class

p true, false
p true.class

p !nil
p !false

# string
name = "hanghang"
puts "I love #{name} , he is my son."
puts 'I and #{name}'  # difference. ' and "

# array
arr = [1,2,3,4,5,6]
puts arr[2] # begin index with 0
print arr[-1]



friends = ["Milhouse", "Ralph", "Nelson", "Otto"]

family = { "Homer" => "dad",
  "Marge" => "mom",
  "Lisa" => "sister",
  "Maggie" => "sister",
  "Abe" => "grandpa",
  "Santa's Little Helper" => "dog"
}

p '*' * 40

food = {
  "Hamburger"=>1.99,
  "Cheese"=>0.99,
  "Steak"=>4.99,
  "Lobster"=>7.99,
  "Fries"=>1.49,
  "Sandwich"=>2.49
}

