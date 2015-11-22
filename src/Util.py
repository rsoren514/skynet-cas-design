def feetToNauticalMiles(feet):
    return float(feet) / 6076.12

def nauticalMilesToFeet(nm):
    return float(nm) * 6076.12

def knotsToFeetPerSecond(knots):
    return nauticalMilesToFeet(knots) / 60 / 60
