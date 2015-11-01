__author__ = 'randy'


class Aircraft:
    def __init__(self):
        self.xInFeet = 0
        self.yInFeet = 0
        self.zInFeet = 0
        self.heading = 0
        self.vSpeedFPS = 0
        self.gSpeedFPS = 0
        self.alertLevel = 0
        self.id = 0

    def getXInFeet(self):
        return self.xInFeet

    def getYInFeet(self):
        return self.yInFeet

    def getZInFeet(self):
        return self.zInFeet

    def getHeading(self):
        return self.heading

    def getVSpeedFPS(self):
        return self.vSpeedFPS

    def getGSpeedFPS(self):
        return self.gSpeedFPS

    def getAlertLevel(self):
        return self.alertLevel

    def calcAlertLevel(self, ownShip):
        return Aircraft()

    def comparePriority(self, other):
        return 0