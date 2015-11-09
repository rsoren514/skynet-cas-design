__author__ = 'randy'

from src.Aircraft import *
from queue import *
from src.Action import *
aircraftQueue = PriorityQueue()


class MainClass:
    def __init__(self):
        self.ownShip = Aircraft(0, 0, 0, 0, 0, 0, 0, 0)
        self.aircraftQueue = PriorityQueue()
        self.myAction = Action(0,0)

    def eventLoop(self):
        while(True):
            return

    def determineAction(self, others:PriorityQueue):
        return

    def setOwnShip(xInFeet: int, yInFeet: int, zInFeet: int,
                 heading: float, vSpeedFPS: int, gSpeedFPS: int,
                 alertLevel: int, id: int):
        ownShip = Aircraft(xInFeet, yInFeet,zInFeet, heading, vSpeedFPS, gSpeedFPS, alertLevel, id)

