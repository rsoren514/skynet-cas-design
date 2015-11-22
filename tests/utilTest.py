import unittest

from src.Util import *


class UtilTest(unittest.TestCase):
    def time_to_collide_test_1(self):
        result = timeToCollide((5, 5), (-1, 0), 1,
                               (-5, 5), (1, 0), 1)
        self.assertEqual(result, (4, 6))
        self.assertEqual(True, False)

if __name__ == "__main__":
    unittest.main()
