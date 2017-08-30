import random

user, sys = 0, 0

class scoreBoard:
    user, sys

    def __init__(self):
        self.user, self.sys = 0, 0

    def increase_user(self):
        self.user += 1

    def increase_sys(self):
        self.sys += 1

    def return_scores(self):
        return self.user, self.sys

def inpoot() :
    TheList = [1,2,3]
    choiceU=input("\t\tCHOICE : ")
    choiceS=random.choice(TheList)
    return int(choiceU), choiceS
