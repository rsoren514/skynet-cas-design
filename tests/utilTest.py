import unittest

from src.Util import *


class UtilTest(unittest.TestCase):

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
