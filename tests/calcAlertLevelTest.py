__author__ = 'AnyaAdmin'
import unittest

from src.Aircraft import *
from src.MainClass import *

from src.Aircraft import *
class AircraftcalcAlertLevelTest(unittest.TestCase):
    def test_alertLv1(self):
        MainClass.setOwnShip(60000,60000,10000,50,30,40,0,1)
        testAircraft = Aircraft(0,0,18000,50,30,40,0,2)
        MainClass.ownShip.calcAlertLevel(testAircraft)
        self.assertEquals(testAircraft.getAlertLevel(), 1)

    def test_alertLv2(self):
        MainClass.setOwnShip(30000,30000,10000,50,30,40,0,1)
        testAircraft = Aircraft(0,0,12500,50,30,40,0,2)
        MainClass.ownShip.calcAlertLevel(testAircraft)
        self.assertEquals(testAircraft.getAlertLevel(), 2)

    def test_alertLv3(self):
        MainClass.setOwnShip(25000,25000,10000,50,30,40,0,1)
        testAircraft = Aircraft(0,0,12500,50,30,40,0,2)
        MainClass.ownShip.calcAlertLevel(testAircraft)
        self.assertEquals(testAircraft.getAlertLevel(), 3)

    def test_alertLv4(self):
        MainClass.setOwnShip(20000,20000,10000,50,30,40,0,1)
        testAircraft = Aircraft(0,0,11600,50,30,40,0,2)
        MainClass.ownShip.calcAlertLevel(testAircraft)
        self.assertEquals(testAircraft.getAlertLevel(), 4)

    def test_alertLv5(self):
        MainClass.setOwnShip(15000,15000,10000,50,30,40,0,1)
        testAircraft = Aircraft(0,0,11000,50,30,40,0,2)
        MainClass.ownShip.calcAlertLevel(testAircraft)
        self.assertEquals(testAircraft.getAlertLevel(), 5)

if __name__ == "__main__":
    unittest.main()