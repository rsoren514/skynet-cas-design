__author__ = 'randy'

from src.Aircraft import *
from queue import *
aircraftQueue = PriorityQueue()


class MainClass:
    def __init__(self):
        self.ownShip = Aircraft(0, 0, 0, 0, 0, 0, 0, 0)
        self.aircraftQueue = PriorityQueue()

    def eventLoop(self):
        while(True):
            return

    def determineAction(self, other:Aircraft):
        return

    def setOwnShip(xInFeet: int, yInFeet: int, zInFeet: int,
                 heading: float, vSpeedFPS: int, gSpeedFPS: int,
                 alertLevel: int, id: int):
        ownShip = Aircraft(xInFeet, yInFeet,zInFeet, heading, vSpeedFPS, gSpeedFPS, alertLevel, id)

