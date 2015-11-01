__author__ = 'randy'

class FrontPanelButtons:
    def __init__(self):
        self.muteBtnDown = False
        self.mapBtnDown = False
        self.defaultBtnDown = False

    def muteBtn(self):
        return self.muteBtnDown

    def mapBtn(self):
        return self.mapBtnDown

    def defaultBtn(self):
        return self.defaultBtnDown
