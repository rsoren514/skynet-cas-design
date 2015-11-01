__author__ = 'randy'


class Action():
    def __init__(self, vsChange: int, urgency: int):
        self.actionVSChange = 0
        self.actionUrgency = 0

    def getVSChange(self):
        return self.actionVSChange

    def getUrgency(self):
        return self.actionUrgency