__author__ = 'randy'

from src.Action import Action
from src.Aircraft import Aircraft

class Display:
    def __init__(self):
        self.mapMode = False
        self.aircraftList = []

    def updateAircraftList(self, aircraftList: []):
        return

    def updateCurAction(self, action: Action):
        return

    def updateCurAlertLevel(self, level: int):
        return

    def setMapMode(self):
        return

    def setDefaultMode(self):
        return
