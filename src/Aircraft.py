__author__ = 'randy'


class Aircraft:
    def __init__(self, xInFeet: int, yInFeet: int, zInFeet: int,
                 heading: float, vSpeedFPS: int, gSpeedFPS: int,
                 alertLevel: int, id: int):
        self.xInFeet = xInFeet
        self.yInFeet = yInFeet
        self.zInFeet = zInFeet
        self.heading = heading
        self.vSpeedFPS = vSpeedFPS
        self.gSpeedFPS = gSpeedFPS
        self.alertLevel = alertLevel
        self.id = id

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
        return Aircraft(0, 0, 0, 0, 0, 0, 0, 0)

    def comparePriority(self, other):
        return 0
