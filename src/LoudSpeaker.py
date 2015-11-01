__author__ = 'randy'

from src.Action import Action


class LoudSpeaker:
    def __init__(self):
        self.lastAction = Action()

    def annunciate(self, action: Action):
        return
