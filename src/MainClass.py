__author__ = 'randy'

from src.Aircraft import *
from queue import *


class MainClass:
    def __init__(self):
        self.ownShip = Aircraft(0, 0, 0, 0, 0, 0, 0, 0)
        self.aircraftQueue = PriorityQueue()

    def eventLoop(self):
        while(True):
            return

    def determineAction(self, other:Aircraft):
        return