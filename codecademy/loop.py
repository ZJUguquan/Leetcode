from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))

    if guess == random_number:
        print 'You win!'
        break

    guesses_left -= 1
if guesses_left == 0:
    print 'You lose'

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade
print_grades(grades)
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total
print grades_sum(grades)
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
print grades_average(grades)

def grades_variance(grades):
    ag = grades_average(grades)
    s = 0
    for grade in grades:
        s += (grade - ag) ** 2
    return s / len(grades)

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** .5




variance = grades_variance(grades)
print grades_std_deviation(variance)