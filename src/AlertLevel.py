__author__ = 'randy'

from enum import Enum

class AlertLevel(Enum):
    AL_NoAlert = 1
    AL_PrevAdvisory = 2
    AL_ResolAdvisoryLow = 3
    AL_ResolAdvisoryMed = 4
    AL_ResolAdvisoryHigh = 5
