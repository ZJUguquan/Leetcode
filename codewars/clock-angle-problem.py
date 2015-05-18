def calculate_angle(hour, minute):
    return int(abs((hour+ minute/60.0)* 30 - minute*6.0)%360)


print calculate_angle(5, 24)