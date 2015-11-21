import unittest

from queue import *
from random import *
from src.Aircraft import *

def get_own_ship(heading: float, v_speed_fps: int, g_speed_fps: int):
    return Aircraft(0, 0, 0, heading, v_speed_fps, g_speed_fps, 0, 0)

def make_random_aircraft(id):
    rng = SystemRandom()
    return Aircraft(
        rng.randint(-100000, 100000),
        rng.randint(-100000, 100000),
        rng.randint(-50000, 50000),
        rng.uniform(0.0, 360.0),
        rng.randint(0, 10000),
        rng.randint(0, 4400),
        rng.randint(0, 5),
        id
    )


class AircraftPriorityQueueTest(unittest.TestCase):
    def test_queue_sorted(self):
        """
        This tests the __lt__ and __eq__ member methods of the
        Aircraft class. A priority queue is used to sort a large
        number of randomly-generated aircraft. The queue is then
        iterated in order to verify that earlier queue items
        should have a higher priority than subsequent queue items.
        """
        pri_queue = PriorityQueue()

        for ac_id in range(0, 5000):
            pri_queue.put(make_random_aircraft(ac_id))

        first = pri_queue.get()
        while not pri_queue.empty():
            second = pri_queue.get()
            self.assertGreaterEqual(first.getAlertLevel(),
                                    second.getAlertLevel())
            if first.getAlertLevel() == second.getAlertLevel():
                self.assertLessEqual(first.distanceToOwnship(),
                                     second.distanceToOwnship())
            first = second

if __name__ == "__main__":
    unittest.main()
