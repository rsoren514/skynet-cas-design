__author__ = 'AnyaAdmin'
import unittest

from src.Aircraft import *
from src.MainClass import *

class AircraftDetermineActionTest(unittest.TestCase):
    def test_doNothing(self):
        MainClass.setOwnShip(0,0,0,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(1,Aircraft(3,3,3,50,30,40,1,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertEquals(0,MainClass.ownShip.myAction.getVSChange())
        self.assertLess(MainClass.ownShip.myAction.getUrgency,0)

    def test_maintain(self):
        MainClass.setOwnShip(0,0,0,50,30,40,0,1)
        MainClass.aircraftQueue.put(2,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,2,4))
        MainClass.aircraftQueue.put(1,Aircraft(3,3,3,50,30,40,1,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertEquals(0,MainClass.ownShip.myAction.getVSChange())
        self.assertGreaterEqual(MainClass.ownShip.myAction.getUrgency(),0)

    def test_maintain(self):
        MainClass.setOwnShip(0,0,0,50,30,40,0,1)
        MainClass.aircraftQueue.put(2,Aircraft(0,0,0,50,30,40,2,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(1,Aircraft(3,3,3,50,30,40,1,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertEquals(0,MainClass.ownShip.myAction.getVSChange())
        self.assertGreaterEqual(MainClass.ownShip.myAction.getUrgency(),0)

    def test_gentleAscend(self):
        MainClass.setOwnShip(0,0,12500,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(3,Aircraft(25000,25000,10000,50,30,40,3,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertGreater(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertLess(MainClass.ownShip.myAction.getUrgency(),0)

    def test_gentleDescend(self):
        MainClass.setOwnShip(0,0,10000,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(3,Aircraft(25000,25000,12500,50,30,40,3,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertLess(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertLess(MainClass.ownShip.myAction.getUrgency(),0)

    def test_normalAscend(self):
        MainClass.setOwnShip(0,0,11600,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(4,Aircraft(20000,20000,10000,50,30,40,4,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertGreater(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertEqual(MainClass.ownShip.myAction.getUrgency(),0)

    def test_normalDescend(self):
        MainClass.setOwnShip(0,0,10000,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(4,Aircraft(20000,20000,11600,50,30,40,4,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertLess(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertEqual(MainClass.ownShip.myAction.getUrgency(),0)

    def test_sharpAscend(self):
        MainClass.setOwnShip(0,0,11000,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(5,Aircraft(15000,15000,10000,50,30,40,5,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertGreater(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertGreater(MainClass.ownShip.myAction.getUrgency(),0)

    def test_sharpDescend(self):
        MainClass.setOwnShip(0,0,10000,50,30,40,0,1)
        MainClass.aircraftQueue.put(1,Aircraft(0,0,0,50,30,40,1,2))
        MainClass.aircraftQueue.put(1,Aircraft(1,1,1,50,30,40,1,3))
        MainClass.aircraftQueue.put(1,Aircraft(2,2,2,50,30,40,1,4))
        MainClass.aircraftQueue.put(5,Aircraft(15000,15000,11000,50,30,40,5,5))
        MainClass.determineAction(MainClass.aircraftQueue())
        self.assertLess(MainClass.ownShip.myAction.getVSChange(),0)
        self.assertGreater(MainClass.ownShip.myAction.getUrgency(),0)