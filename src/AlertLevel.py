__author__ = 'randy'

from enum import *

class AlertLevel(IntEnum):
    AL_NoAlert = 1
    AL_PrevAdvisory = 2
    AL_ResolAdvisoryLow = 3
    AL_ResolAdvisoryMed = 4
    AL_ResolAdvisoryHigh = 5
