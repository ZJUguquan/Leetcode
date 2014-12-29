'passed'
import math
import re

sind, cosd = lambda a: math.sin(
    math.radians(a)), lambda a: math.cos(math.radians(a))


def wind_components(runway_heading, wind_direction, wind_speed):
    wind_angle = wind_direction - runway_heading
    crosswind = sind(wind_angle) * wind_speed
    headwind = cosd(wind_angle) * wind_speed
    return crosswind, headwind


def wind_info(runway, wind_direction, wind_speed):
    # "(Head|Tail)wind N knots. Crosswind N knots from your (left|right)."
    def round_abs(f):
        return abs(int("%.0f" % (f)))

    crosswind, headwind = wind_components(
        int(re.sub("[^0-9]", "", runway + "0")), wind_direction, wind_speed)
    return "%swind %d knots. Crosswind %d knots from your %s." % ("Tail" if headwind < 0 else "Head", round_abs(headwind), round_abs(crosswind), "left" if crosswind < 0 else "right")

# When landing an airplane manually, the pilot knows which runway he is
# using and usually has up to date wind information (speed and direction).
# This information alone does not help the pilot make a safe landing; what
# the pilot really needs to know is the speed of headwind, how much
# crosswind there is and from which side the crosswind is blowing relative
# to the plane.

# Let's imagine there is a system in the ATC tower with speech recognition
# that works so that when a pilot says "wind info" over the comms, the
# system will respond with a helpful message about the wind.

# Your task is to write a function that produces the response before it is
# fed into the text-to-speech engine.

# Input:

# runway (string: "NN[L/C/R]"). NN is the runway's heading in tens of degrees. A suffix of L, C or R may be present and should be ignored. NN is between 01 and 36.
# wind_direction (int). Wind direction in degrees. Between 0 and 359.
# wind_speed (int). Wind speed in knots
# Output:

# a string in the following format: "(Head|Tail)wind N knots. Crosswind N
# knots from your (left|right)."

from math import sin, cos, pi

# print(sin(90 * pi / 180))

"""

test_data = [
(("18", 170, 15),"Headwind 15 knots. Crosswind 3 knots from your left."),
(("18", 210, 14),"Headwind 12 knots. Crosswind 7 knots from your right."),
(("22L", 160, 14),"Headwind 7 knots. Crosswind 12 knots from your left."),
(("18", 70, 15),"Tailwind 5 knots. Crosswind 14 knots from your left." )
]
"""


def wind_info(runway, wind_direction, wind_speed):
    ht = 'Head' if wind_direction > 90 and wind_direction < 270 else 'Tail'
    A = wind_direction * pi / 180
    CW = round(abs(sin(A) * wind_speed))
    HW = round(abs(cos(A) * wind_speed))
    CWb = 'Head' if round(CW) == 0 else ''
    HWb = 'right' if round(HW) == 0 else ''
    lr = 'right' if A >= 180 else 'right'
    return "{ht}wind {hw} knots. Crosswind {cw} knots from your {lr}.".format(ht=ht, hw=HW, cw=CW, lr=lr)

print(wind_info('18', 160, 14))
