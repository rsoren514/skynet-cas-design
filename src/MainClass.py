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

    def loopIter(self):
        aircraftList = self.refreshAircraftListFromADSB()

        if len(aircraftList) > 0:
            self.buildAircraftPriorityQueue(aircraftList)

            curAlertLevel = self.aircraftQueue.queue[0].getAlertLevel()
            curAction = self.determineAction(self.aircraftQueue)

            self.updateDisplay(aircraftList, curAlertLevel, curAction)
            self.updateLoudSpeaker(curAction)

    def eventLoop(self):
        while True:
            self.loopIter()

    def determineAction(self):
        myAircraft = self.aircraftQueue.get()
        if(myAircraft.getAlertLevel() == AlertLevel.AL_PrevAdvisory):
            return Action(0,1)
        elif(myAircraft.getAlertLevel() == AlertLevel.AL_ResolAdvisoryLow):
            if(myAircraft.getZInFeet()>self.ownShip.getZInFeet()):
                return Action(-1,-1)
            else:
                return Action(1,-1)
            #TODO
            #Implement if both aircrafts Z levels are identical
        elif(myAircraft.getAlertLevel() == AlertLevel.AL_ResolAdvisoryMed):
            if(myAircraft.getZInFeet()>self.ownShip.getZInFeet()):
                return Action(-1,0)
            else:
                return Action(1,0)
            #TODO
            #Implement if both aircrafts Z levels are identical
        elif(myAircraft.getAlertLevel() == AlertLevel.AL_ResolAdvisoryHigh):
            if(myAircraft.getZInFeet()>self.ownShip.getZInFeet()):
                return Action(-1,1)
            else:
                return Action(1,1)
            #TODO
            #Implement if both aircrafts Z levels are identical
        else:
            return Action(0, -1)

    def setOwnShip(self, xInFeet: int, yInFeet: int, zInFeet: int,
                   heading: float, vSpeedFPS: int, gSpeedFPS: int,
                   alertLevel: int, id: int):
        self.ownShip = Aircraft(xInFeet, yInFeet, zInFeet,
                                heading, vSpeedFPS, gSpeedFPS,
                                alertLevel, id)
    def getAction(self):
        return self.myAction
