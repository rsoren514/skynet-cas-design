import unittest

from src.Util import *


def check_result_row(row, test_obj: unittest.TestCase):
    if type(row[0]) == float:
        test_obj.assertAlmostEqual(row[0], row[1], places=row[2])
    elif type(row[0]) == int:
        test_obj.assertEqual(row[0], row[1])
    elif type(row[0]) == tuple: # e.g. (tuple, tuple, int)
        for i in range(0, len(row[0])):
            check_result_row((row[0][i], row[1][i], row[2]), test_obj)


def check_result_table(results, test_obj: unittest.TestCase):
    for row in results:
        check_result_row(row, test_obj)


class UtilTest(unittest.TestCase):

    #
    # Unit Conversion Tests
    #
    # Google was used as a reference calculator to obtain results
    # to these particular tests. The conversion functions being
    # tested are based on unit conversion data from NIST (see
    # Util.py).
    #
    # Our stuff is actually more precise than Google's, so we
    # only check for as much precision as Google provides.
    #

    def test_feet_to_nautical_miles(self):
        results = [
            # (our result, Google result, places of accuracy)
            (feetToNauticalMiles(2746.8), 0.45206514, 8),
            (feetToNauticalMiles(1.0), 0.000164579, 9),
            (feetToNauticalMiles(-1.0), -0.000164579, 9),
            (feetToNauticalMiles(1000000.0), 164.578834, 6),
            (feetToNauticalMiles(123456789.123456789), 20318.374365458763, 12),
            (feetToNauticalMiles(0.0000001), 1.64579e-11, 16),
        ]

        check_result_table(results, self)
        self.assertEqual(feetToNauticalMiles(0.0), 0.0)

    def test_nautical_miles_to_feet(self):
        results = [
            # (our result, Google result, places of accuracy)
            (nauticalMilesToFeet(6349.532), 38580489.711, 3),
            (nauticalMilesToFeet(5.0), 30380.6, 1),
            (nauticalMilesToFeet(-5.0), -30380.6, 1),
            (nauticalMilesToFeet(0.000001), 0.00607612, 8),
            (nauticalMilesToFeet(8675309.0), 5.2712179e+10, -3),
            (nauticalMilesToFeet(1987.03), 12073423.75, 2),
        ]

        check_result_table(results, self)
        self.assertEqual(nauticalMilesToFeet(0.0), 0.0)

    def test_knots_to_feet_per_second(self):
        #
        # Some of these results were rounded up to a 1/100th of a
        # foot as Google's results don't appear to be precise,
        # whether you convert to knots per second first or to feet
        # per hour first.
        #
        results = [
            # (our result, Google result, places of accuracy)
            (knotsToFeetPerSecond(200.0), 337.561971, 6),
            (knotsToFeetPerSecond(120.0), 202.537183, 6),
            (knotsToFeetPerSecond(1987.03), 3353.73, 2),
            (knotsToFeetPerSecond(0.000001), 1.68781e-6, 12),
            (knotsToFeetPerSecond(667.76), 1127.05191, 5)
        ]
        check_result_table(results, self)
        self.assertEqual(knotsToFeetPerSecond(0.0), 0.0)

    #
    # Misc. Tests
    #

    def test_dot_product(self):
        results = [
            (dotProduct((2, 3), (4, 5)), 23, 100),
            (dotProduct((-4.25, 2.37), (8.6, 9.75)), -13.4425, 4),
            (dotProduct((0, 0), (0, 0)), 0, 100),
        ]
        check_result_table(results, self)

    def test_velocity(self):
        results = [
            (velocity(0, 1), (0, 1), 15),
            (velocity(360, 1), (0, 1), 15),
            (velocity(90, 1), (1, 0), 15),
            (velocity(180, 1), (0, -1), 15),
            (velocity(270, 2), (-2, 0), 15),
            (velocity(45, sqrt(2)), (1, 1), 15),
            (velocity(225, sqrt(2)), (-1, -1), 15)
        ]
        check_result_table(results, self)

    #
    # Circle Collision Tests
    #

    def test_time_to_collide_will_collide_1(self):
        """
        Two circles with radius 1 distance unit are moving
        straight at each other. Each has a velocity of 1 distance
        unit per time unit. Their centers are 10 distance units
        apart, and thus their edges are 8 distance units apart.
        They should begin colliding after 4 time units and stop
        colliding after 6 time units.
        """

        result = timeToCollide((5, 5), (-1, 0), 1,
                               (-5, 5), (1, 0), 1)
        self.assertNotEqual(result, False)
        self.assertLess(result[0], result[1])
        self.assertEqual(result, (4.0, 6.0))

    def test_time_to_collide_will_collide_2(self):
        """
        Similar to the above test except the circles are displaced
        such that their outer boundaries will only contact at a
        single instant (5 time units).
        """
        result = timeToCollide((5, 6), (-1, 0), 1,
                               (-5, 4), (1, 0), 1)
        self.assertNotEqual(result, False)
        self.assertLessEqual(result[0], result[1])
        self.assertEqual(result, (5.0, 5.0))

    def test_time_to_collide_will_collide_3(self):
        """
        Similar to the above test except the circles are moving
        at each other vertically (on the Y-axis) instead of
        horizontally (on the X-axis).
        """
        result = timeToCollide((5, 5), (0, -1), 1,
                               (5, -5), (0, 1), 1)
        self.assertNotEqual(result, False)
        self.assertLess(result[0], result[1])
        self.assertEqual(result, (4.0, 6.0))

    def test_time_to_collide_wont_collide_1(self):
        """
        Similar to the above test except the circles are displaced
        such that there hasn't been, and will not be, a collision.
        """

        result = timeToCollide((5, 5), (1, 0), 1,
                               (-5, -5), (-1, 0), 1)
        self.assertFalse(result)

    def test_time_to_collide_mid_collision_1(self):
        """
        In this test the circles already started to collide 0.5
        time units ago, and will not stop for another 1.5 time
        units.
        """

        result = timeToCollide((0.5, 5), (-1, 0), 1,
                               (-0.5, 5), (1, 0), 1)
        self.assertNotEqual(result, False)
        self.assertLess(result[0], result[1])
        self.assertLess(result[0], 0.0)
        self.assertGreater(result[1], 0.0)
        self.assertEqual(result, (-0.5, 1.5))

    def test_time_to_collide_already_collided_1(self):
        """
        In this test the circles already started to collide 6.0
        time units ago and stopped colliding 4.0 time units ago.
        """
        result = timeToCollide((5, 5), (1, 0), 1,
                               (-5, 5), (-1, 0), 1)
        self.assertNotEqual(result, False)
        self.assertLess(result[0], result[1])
        self.assertEqual(result, (-6.0, -4.0))


if __name__ == "__main__":
    unittest.main()
