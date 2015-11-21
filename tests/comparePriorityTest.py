__author__ = 'AnyaAdmin'
import unittest

from src.Aircraft import *


def get_own_ship(heading: float, v_speed_fps: int, g_speed_fps: int):
    return Aircraft(0, 0, 0, heading, v_speed_fps, g_speed_fps, 0, 0)

def do_compare_a_to_b(own_ship: Aircraft, aircraft_a: Aircraft,
                      aircraft_b: Aircraft):
    aircraft_a.calcAlertLevel(own_ship)
    aircraft_b.calcAlertLevel(own_ship)

    return aircraft_a.comparePriority(aircraft_b)

class AircraftComparePriorityTest(unittest.TestCase):
    def test_horiz_closer_gt(self):
        own_ship = get_own_ship(0.0, 0, 220)
        h_closer = Aircraft(0, 2000, 0, 180.0, 0, 220, 0, 1)
        h_farther = Aircraft(0, 20000, 0, 180.0, 0, 220, 0, 2)

        result = do_compare_a_to_b(own_ship, h_closer, h_farther)
        self.assertLess(result, 0)

    def test_vert_closer_gt(self):
        own_ship = get_own_ship(0.0, 0, 220)
        v_closer = Aircraft(0, 5280, 0, 180.0, 0, 220, 0, 1)
        v_farther = Aircraft(0, 5280, 1000, 180.0, 0, 220, 0, 1)

        result = do_compare_a_to_b(own_ship, v_closer, v_farther)
        self.assertLess(result, 0)

    def test_equal_dist_equal_priority(self):
        own_ship = get_own_ship(0.0, 0, 220)
        aircraft_a = Aircraft(5280, 5280, 0, 180.0, 0, 220, 0, 1)
        aircraft_b = Aircraft(-5280, 5280, 0, 180.0, 0, 220, 0, 2)

        result = do_compare_a_to_b(own_ship, aircraft_a, aircraft_b)
        self.assertEqual(0, result)

    def test_far_away_equal_priority(self):
        own_ship = get_own_ship(0.0, 0, 220)
        aircraft_a = Aircraft(100000, 0, 0, 270.0, 0, 220, 0, 1)
        aircraft_b = Aircraft(-100000, 0, 0, 90.0, 0, 220, 0, 2)

        result = do_compare_a_to_b(own_ship, aircraft_a, aircraft_b)
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
