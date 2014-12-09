def calculate_optimal_fare(D, T, V1, R, V2):
    # TODO: return minimal taxi fare (e.g. "3.14") or "Won't make it!"
    max_hour = T/60.0
    if V1 < 0.0001:
        taxi_hour = T + 5000
    else:
        taxi_hour = D/V1
    if V2 < 0.000001:
        walk_hour = T + 5000
    else:
        walk_hour = D/V2
    if min(taxi_hour, walk_hour) > max_hour:
        return """Won't make it!"""
    if V2 >= V1 or walk_hour <= max_hour:
        return "0.00"
    # must take taxi
    hour_diff = walk_hour - max_hour
    print(walk_hour, max_hour)
    d1 = hour_diff * (V1*V2)/(V1-V2)
    res = d1 * R
    return format(res,'.2f')


print(calculate_optimal_fare(100, 10, 500, 5, 25))
print(calculate_optimal_fare(8, 10, 90, 2, 6))
# test.assert_equals(calculate_optimal_fare(8, 10, 90, 2, 6), "15.00")
# test.assert_equals(calculate_optimal_fare(100, 10, 500, 5, 25), "Won't make it!")

 # The student needs to get on a train that leaves from the station D kilometres away in T minutes.
# She can get a taxi that drives at V1 km/h for the price of R €/km or she can walk at V2 km/h for free.

# A correct solution will be a function that returns the minimum price she needs to pay the taxi driver or the string "Won't make it!".

# All the inputs will be positive integers, the output has to be a string containing a number with two decimal places - or "Won't make it!" if that is the case.

# It won't take her any time to get on the taxi or the train.

# # In non-trivial cases you need to combine walking and riding the taxi so that she makes it, but pays as little as possible.