from math import *

def feetToNauticalMiles(feet):
    return float(feet) / 6076.12

def nauticalMilesToFeet(nm):
    return float(nm) * 6076.12

def knotsToFeetPerSecond(knots):
    return nauticalMilesToFeet(knots) / 60 / 60

def dotProduct(p0, p1):
    return p0[0] * p1[0] + p0[1] * p1[1]

def timeToCollide(c0, v0, r0, c1, v1, r1):
    """
    Determine the start and stop times of collision of two circles
    moving on a plane.

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

    root = sqrt((d_dot_w * d_dot_w) - (w_dot_w * (d_dot_d - (sum_r * sum_r))))

    t0 = (-d_dot_w + root) / w_dot_w
    t1 = (-d_dot_w - root) / w_dot_w

    return tuple(sorted((t0, t1)))