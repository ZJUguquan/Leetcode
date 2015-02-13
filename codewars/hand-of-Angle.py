

import math
def handAngle(hours, minutes):
    degrees = abs(.5 * (60 * hours + minutes) - 6 * minutes)
    if degrees > 180:
        degrees = 360 - degrees
    return (math.pi / 180) * degrees