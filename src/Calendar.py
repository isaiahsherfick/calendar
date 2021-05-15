from Year import *
import os


class Calendar:
    def __init__(self):
        self.years = {}
        for i in range(2021,2122):
            self.years.update({i:Year(i)})
    def save(self):
        f = open("../cal/isaiahs_calendar","w")
        for y in self.years:


    def load(self):
        f = open("../cal/isaiahs_calendar","w")

