import random
import math
import datetime


class Weather:
    def __init__(self):
        self.season = ""

    def get_season(self, date):
        year = date.year
        seasons = [('winter', (datetime.date(year, 1, 1), datetime.date(year, 3, 20))),
                   ('spring', (datetime.date(year, 3, 21), datetime.date(year, 6, 20))),
                   ('summer', (datetime.date(year, 6, 21), datetime.date(year, 9, 22))),
                   ('autumn', (datetime.date(year, 9, 23), datetime.date(year, 12, 20))),
                   ('winter', (datetime.date(year, 12, 21), datetime.date(year, 12, 31)))]
        for self.season, (start, end) in seasons:
            if start <= date <= end:
                return self.season

    def get_temp(self):
        mean = 0
        std_dev = 10
        if self.season == "winter":
            mean = (45 + (-32)) / 2.5
            std_dev = 5
        elif self.season == "spring" or self.season == "autumn":
            mean = (45 + (-32)) / 1.8
            std_dev = 15
        else:
            mean = (45 + (-32)) / 1.3
            std_dev = 10


        while True:
            degrees_c = round(random.normalvariate(mean, std_dev))
            degrees_f = math.floor(degrees_c * 9 / 5 + 32)
            degrees_k = math.floor(degrees_c + 273.15)
            if -32 <= degrees_c <= 45:
                break
        print(f"{degrees_c} C")
        print(f"{degrees_f} F")
        print(f"{degrees_k} K")
