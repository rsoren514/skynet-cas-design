__author__ = 'randy'

from src.ADS_BDataFrame import *
from src.ADS_BDataProcessor import *
from src.ADS_BDriver import *
from src.Action import *
from src.Aircraft import *
from src.Display import *
from src.FrontPanelButtons import *
from src.LoudSpeaker import *
from queue import *

aircraftQueue = PriorityQueue()


class MainClass:
    def __init__(self):
        self.ownShip = Aircraft(0, 0, 0, 0, 0, 0, 0, 0)
        self.aircraftQueue = PriorityQueue()
        self.myAction = Action(0,0)
        self.ads_bInt = ADS_BDriver()
        self.display = Display()
        self.loudSpeaker = LoudSpeaker()
        self.panelBtns = FrontPanelButtons()

    def refreshAircraftListFromADSB(self):
        adsData = self.ads_bInt.refresh()
        return ADS_BDataProcessor.getAircraftList(adsData)

    def buildAircraftPriorityQueue(self, aircraftList):
        self.aircraftQueue = PriorityQueue()
        for a in aircraftList:
            self.aircraftQueue.put(a)

    def updateDisplay(self, aircraftList, alertLevel, action):
        self.display.updateAircraftList(aircraftList)
        self.display.updateCurAlertLevel(alertLevel)
        self.display.updateCurAction(action)

    def updateLoudSpeaker(self, action):
        self.loudSpeaker.annunciate(action)

    def eventLoop(self):
        while True:
            aircraftList = self.refreshAircraftListFromADSB()

            if len(aircraftList) > 0:
                self.buildAircraftPriorityQueue(aircraftList)

                curAlertLevel = self.aircraftQueue.queue[0].getAlertLevel()
                curAction = self.determineAction(self.aircraftQueue)

                self.updateDisplay(aircraftList, curAlertLevel, curAction)
                self.updateLoudSpeaker(curAction)

    def determineAction(self, others: PriorityQueue):
        return Action(0, 0)

    def setOwnShip(self, xInFeet: int, yInFeet: int, zInFeet: int,
                   heading: float, vSpeedFPS: int, gSpeedFPS: int,
                   alertLevel: int, id: int):
        self.ownShip = Aircraft(xInFeet, yInFeet, zInFeet,
                                heading, vSpeedFPS, gSpeedFPS,
                                alertLevel, id)

