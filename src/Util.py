from math import *

#
# One nautical mile is exactly 1,852 meters.
#       (http://physics.nist.gov/cuu/Units/outside.html)
#
# One foot is exactly 0.3048 meters.
#       (http://physics.nist.gov/Pubs/SP811/appenB.html)
#       (ftp://ftp.nist.gov/pub/dataplot/other/reference/CONVFACT.TXT)
#
FEET_PER_NAUTICAL_MILE = 1852.0 / 0.3048
NAUTICAL_MILES_PER_FOOT = 0.3048 / 1852.0

def feetToNauticalMiles(feet):
    return float(feet) / FEET_PER_NAUTICAL_MILE


def nauticalMilesToFeet(nm):
    return float(nm) * FEET_PER_NAUTICAL_MILE


def knotsToFeetPerSecond(knots):
    return nauticalMilesToFeet(knots) / 60.0 / 60.0


def dotProduct(p0, p1):
    return (p0[0] * p1[0]) + (p0[1] * p1[1])


def velocity(headingDegrees, speedFPS):
    return (sin(radians(headingDegrees)) * speedFPS,
            cos(radians(headingDegrees)) * speedFPS)


def timeToCollide(c0, v0, r0, c1, v1, r1):
    """
    Determine the start and stop times of collision of two circles
    moving on a geometric plane.

    :param c0: First circle's center position tuple.
    :param v0: First circle's velocity tuple.
    :param r0: First circle's radius.
    :param c1: Second circle's center position tuple.
    :param v1: Second circle's velocity tuple.
    :param r1: Second circle's radius.
    :return: (start, stop) time of collision tuple.
    """

    d = (c0[0] - c1[0], c0[1] - c1[1])
    w = (v0[0] - v1[0], v0[1] - v1[1])

    d_dot_w = dotProduct(d, w)
    d_dot_d = dotProduct(d, d)
    w_dot_w = dotProduct(w, w)
    sum_r = r0 + r1

    try:
        root = sqrt((d_dot_w * d_dot_w) -
                    (w_dot_w * (d_dot_d - (sum_r * sum_r))))
    except ValueError:
        return False

    t0 = (-d_dot_w + root) / w_dot_w
    t1 = (-d_dot_w - root) / w_dot_w

    return tuple(sorted((t0, t1)))
