__author__ = 'AnyaAdmin'
import unittest

from src.Aircraft import *
from src.MainClass import *

class AircraftDetermineActionTest(unittest.TestCase):
    def test_doNothing(self):
        main = MainClass()
        main.setOwnShip(0,0,0,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(3,3,3,50,30,40,AlertLevel.AL_NoAlert,5))
        testAction = main.determineAction
        self.assertEquals(0,testAction.getVSChange())
        self.assertLess(testAction.getUrgency(),0)

    def test_maintain(self):
        main = MainClass()
        main.setOwnShip(0,0,0,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_PrevAdvisory,4))
        main.aircraftQueue.put(Aircraft(3,3,3,50,30,40,AlertLevel.AL_NoAlert,5))
        testAction = main.determineAction
        self.assertEquals(0,testAction.getVSChange())
        self.assertGreaterEqual(testAction.getUrgency(),0)

    def test_maintain2(self):
        main = MainClass()
        main.setOwnShip(0,0,0,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_PrevAdvisory,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(3,3,3,50,30,40,AlertLevel.AL_NoAlert,5))
        testAction = main.determineAction
        self.assertEquals(0,testAction.getVSChange())
        self.assertGreaterEqual(testAction.getUrgency(),0)

    def test_gentleAscend(self):
        main = MainClass()
        main.setOwnShip(0,0,12500,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(25000,25000,10000,50,30,40,AlertLevel.AL_ResolAdvisoryLow,5))
        testAction = main.determineAction
        self.assertGreater(testAction.getVSChange(),0)
        self.assertLess(testAction.getUrgency(),0)

    def test_gentleDescend(self):
        main = MainClass()
        main.setOwnShip(0,0,10000,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(25000,25000,12500,50,30,40,AlertLevel.AL_ResolAdvisoryLow,5))
        testAction = main.determineAction
        self.assertLess(testAction.getVSChange(),0)
        self.assertLess(testAction.getUrgency(),0)

    def test_normalAscend(self):
        main = MainClass()
        main.setOwnShip(0,0,11600,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(20000,20000,10000,50,30,40,AlertLevel.AL_ResolAdvisoryMed,5))
        testAction = main.determineAction
        self.assertGreater(testAction.getVSChange(),0)
        self.assertEqual(testAction.getUrgency(),0)

    def test_normalDescend(self):
        main = MainClass()
        main.setOwnShip(0,0,10000,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(20000,20000,11600,50,30,40,AlertLevel.AL_ResolAdvisoryMed,5))
        testAction = main.determineAction
        self.assertLess(testAction.getVSChange(),0)
        self.assertEqual(testAction.getUrgency(),0)

    def test_sharpAscend(self):
        main = MainClass()
        main.setOwnShip(0,0,11000,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(15000,15000,10000,50,30,40,AlertLevel.AL_ResolAdvisoryHigh,5))
        testAction = main.determineAction
        self.assertGreater(testAction.getVSChange(),0)
        self.assertGreater(testAction.getUrgency(),0)

    def test_sharpDescend(self):
        main = MainClass()
        main.setOwnShip(0,0,10000,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(15000,15000,11000,50,30,40,AlertLevel.AL_ResolAdvisoryHigh,5))
        testAction = main.determineAction
        self.assertLess(testAction.getVSChange(),0)
        self.assertGreater(testAction.getUrgency(),0)

    def test_sharpDescendEqualZ(self):
        main = MainClass()
        main.setOwnShip(0,14000,11000,50,40,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(15000,15000,11000,50,30,40,AlertLevel.AL_ResolAdvisoryHigh,5))
        testAction = main.determineAction
        self.assertLess(testAction.getVSChange(),0)
        self.assertGreater(testAction.getUrgency(),0)

    def test_normalAscendEqualZY(self):
        main = MainClass()
        main.setOwnShip(21000,20000,10000,50,30,40,0,1)
        main.aircraftQueue.put(Aircraft(0,0,0,50,30,40,AlertLevel.AL_NoAlert,2))
        main.aircraftQueue.put(Aircraft(1,1,1,50,30,40,AlertLevel.AL_NoAlert,3))
        main.aircraftQueue.put(Aircraft(2,2,2,50,30,40,AlertLevel.AL_NoAlert,4))
        main.aircraftQueue.put(Aircraft(20000,20000,10000,50,30,40,AlertLevel.AL_ResolAdvisoryMed,5))
        testAction = main.determineAction
        self.assertGreater(testAction.getVSChange(),0)
        self.assertEqual(testAction.getUrgency(),0)

if __name__ == "__main__":
    unittest.main()