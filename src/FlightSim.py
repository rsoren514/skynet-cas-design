import math

class AircraftSim:
    __xInFeet = 0.0
    __yInFeet = 0.0
    __zInFeet = 0.0
    __heading = 0.0
    __vSpeedFPS = 0.0
    __gSpeedFPS = 0.0
    __aircraftID = ""

    def __init__(self, airID, x=None, y=None, z=None, heading=None, vSpeed=None ):
        if x is not None and y is not None and z is not None and heading is not None and vSpeed is not None:
            self.__aircraftID = airID
            self.__xInFeet = x
            self.__yInFeet = y
            self.__zInFeet = z
            self.__heading = heading
            self.__vSpeedFPS = vSpeed
        else:
            self.__aircraftID = airID

    def addZ(self):
        self.__zInFeet += 10

    def subZ(self):
        self.__zInFeet -= 10

    def printPos(self):
        print ("Aircraft ID is: " + self.__aircraftID)
        print ("X: " + str(self.__xInFeet))
        print ("Y: " + str(self.__yInFeet))
        print ("Z: " + str(self.__zInFeet))
        print ("The VSpeed is " + str(self.__vSpeedFPS))
        print ("The heading is " + str(self.__heading))

    def printChange(self, x, y, z):
        print ("Change in X :" + str(x))
        print ("Change in Y :" + str(y))
        print ("Change in Z :" + str(z))

    #assuming we are getting new information every second
    def calcMovement(self):
        if self.__heading >=0 and self.__heading <= 90:
            x1 = self.__vSpeedFPS * math.sin(math.radians(self.__heading))
            y1 = self.__vSpeedFPS * math.cos(math.radians(self.__heading))
            # self.printChange(x1, y1, self.__zInFeet)
            self.__xInFeet = self.__xInFeet + x1
            self.__yInFeet = self.__yInFeet + y1
        elif self.__heading > 90 and self.__heading <= 180:
            y1 = self.__vSpeedFPS * math.sin(math.radians(self.__heading - 90))
            x1 = self.__vSpeedFPS * math.cos(math.radians(self.__heading - 90))
            # self.printChange(x1, y1, self.__zInFeet)
            self.__xInFeet = self.__xInFeet + x1
            self.__yInFeet = self.__yInFeet - y1
        elif self.__heading > 180 and self.__heading <= 270:
            x1 = self.__vSpeedFPS * math.sin(math.radians(self.__heading - 180))
            y1 = self.__vSpeedFPS * math.cos(math.radians(self.__heading - 180))
            # self.printChange(x1, y1, self.__zInFeet)
            self.__xInFeet = self.__xInFeet - x1
            self.__yInFeet = self.__yInFeet - y1
        elif self.__heading > 270 and self.__heading <= 360:
            x1 = self.__vSpeedFPS * math.sin(math.radians(360 - self.__heading))
            y1 = self.__vSpeedFPS * math.cos(math.radians(360 - self.__heading))
            # self.printChange(x1, y1, self.__zInFeet)
            self.__xInFeet = self.__xInFeet - x1
            self.__yInFeet = self.__yInFeet + y1

    #Turns x, y, z coordinates from 1st and 2nd aircraft into x, y, z with 1st aircraft as orgin (0,0,0)
    def mkOwnershipOrgin(self, otherAircraft ):
        x = self.__xInFeet
        y = self.__yInFeet
        z = self.__zInFeet
        if x == 0:
            return
        else:
            if x > 0:
                otherAircraft.__xInFeet = otherAircraft.__xInFeet - x
                # print otherAircraft.__xInFeet
                self.__xInFeet = self.__xInFeet - x
            else:
                otherAircraft.__xInFeet = otherAircraft.__xInFeet + x
                # print otherAircraft.__xInFeet
                self.__xInFeet = self.__xInFeet + x
        if y == 0:
            return
        else:
            if y > 0:
                otherAircraft.__yInFeet = otherAircraft.__yInFeet - y
                # print otherAircraft.__yInFeet
                self.__yInFeet = self.__yInFeet - y
            else:
                otherAircraft.__yInFeet = otherAircraft.__yInFeet + y
                # print otherAircraft.__yInFeet
                self.__yInFeet = self.__yInFeet + y
        if z == 0:
            return
        else:
            if z > 0:
                otherAircraft.__zInFeet = otherAircraft.__zInFeet - z
                # print otherAircraft.__zInFeet
                self.__zInFeet = self.__zInFeet - z
            else:
                otherAircraft.__zInFeet = otherAircraft.__zInFeet + z
                # print otherAircraft.__zInFeet
                self.__zInFeet = self.__zInFeet + z


#the part that runs a sim of what happens in a second

air1 = AircraftSim('0001', 0, 0, 0, 90, 1)
air1.printPos()
air2 = AircraftSim('0002', 10, 10, 0, 270, 1)
air2.printPos()
air1.mkOwnershipOrgin(air2)
air1.printPos()
air2.printPos()

import Tkinter

window = Tkinter.Tk()
window.minsize(800, 600)

def doAStep():
    air1.calcMovement()
    air2.calcMovement()
    air1.mkOwnershipOrgin(air2)
    air1.printPos()
    air2.printPos()

B = Tkinter.Button(window, text ="Advance 1 sec", command = doAStep)

B.pack()
window.mainloop()