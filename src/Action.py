__author__ = 'randy'


class Action():
    def __init__(self, vsChange: int, urgency: int):
        self.actionVSChange = vsChange
        self.actionUrgency = urgency

    def getVSChange(self):
        return self.actionVSChange

    def getUrgency(self):
        return self.actionUrgency
