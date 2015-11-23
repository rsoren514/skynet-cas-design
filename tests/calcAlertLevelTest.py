__author__ = 'AnyaAdmin'
import unittest

from src.MainClass import *
from src.Aircraft import *

class AircraftcalcAlertLevelTest(unittest.TestCase):
    def test_alertLv1(self):
        main = MainClass()
        testAircraft = Aircraft(60000,60000,8000,50,30,40,0,1)
        testAircraft.calcAlertLevel(main.ownShip)
        self.assertEquals(testAircraft.getAlertLevel(), 1)

    def test_alertLv2(self):
        main = MainClass()
        testAircraft = Aircraft(0,35000,2500,270,0,200,0,1)
        testAircraft.calcAlertLevel(main.ownShip)
        self.assertEquals(testAircraft.getAlertLevel(), 2)

    def test_alertLv3(self):
        main = MainClass()
        testAircraft = Aircraft(0,35000,2500,180,0,200,0,1)
        testAircraft.calcAlertLevel(main.ownShip)
        self.assertEquals(testAircraft.getAlertLevel(), 3)

    def test_alertLv4(self):
        main = MainClass()
        testAircraft = Aircraft(20000,20000,1600,50,30,40,0,1)
        testAircraft.calcAlertLevel(main.ownShip)
        self.assertEquals(testAircraft.getAlertLevel(), 4)

    def test_alertLv5(self):
        main = MainClass()
        testAircraft = Aircraft(15000,15000,1000,50,30,40,0,1)
        testAircraft.calcAlertLevel(main.ownShip)
        self.assertEquals(testAircraft.getAlertLevel(), 5)

if __name__ == "__main__":
    unittest.main()
