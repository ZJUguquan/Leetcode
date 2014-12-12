import math
EPSILON = 0.01
N = 10
UNIT = EPSILON**2 / N**2

"ANSWERS"

NUM_SAMPLES = 100000

def area_of_the_shape(f):
    sum = 0.0
    for i in range(NUM_SAMPLES):
        x = random.random()
        y = random.random()
        sum += 1.0 if f(x, y) else 0.0
    return sum / NUM_SAMPLES


def myrange(start, stop, step):
	while start <= stop:
		yield start
		start += step

# for i in myrange(1,3,0.5):print(i)

def area_of_the_shape(f):
	area = 0
	for x in myrange(0, 1, EPSILON/N):
		for y in myrange(0, 1, EPSILON/N):
			if f(x, y):
				area += UNIT

	return area

def circular_area(x, y):
  if (x - 0.5) ** 2 + (y - 0.5) ** 2 <= 0.25:
    return True
  return False

def full_shape(x, y):
  if 0 < x < 1 and 0 < y < 1:
    return True
  return False

print(abs(area_of_the_shape(circular_area) - 0.25 * math.pi))
# Test.expect(abs(area_of_the_shape(circular_area) - 0.25 * math.pi) <= EPSILON, "On testing a circular shape bounded by the area")
# Test.expect(abs(area_of_the_shape(full_shape) - 1) <= EPSILON, "On testing the whole area")
#