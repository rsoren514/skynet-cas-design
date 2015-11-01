__author__ = 'randy'

from src.Aircraft import *
from queue import *


class MainClass:
    def __init__(self):
        self.ownShip = Aircraft()
        self.aircraftQueue = PriorityQueue()
