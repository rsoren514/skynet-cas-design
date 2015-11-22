import unittest

from src.Util import *


class UtilTest(unittest.TestCase):
    def test_time_to_collide_1(self):
        result = timeToCollide((5, 5), (-1, 0), 1,
                               (-5, 5), (1, 0), 1)
        self.assertLess(result[0], result[1])
        self.assertEqual(result, (4, 6))

    def test_time_to_collide_2(self):
        result = timeToCollide((5, 5), (1, 0), 1,
                               (-5, -5), (-1, 0), 1)
        print(result)

if __name__ == "__main__":
    unittest.main()
