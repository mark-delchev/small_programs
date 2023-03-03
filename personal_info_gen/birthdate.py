import random
import datetime
import numpy as np
from faker import Faker
from transliterate import translit


class Person:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.personal_number = ""
        self.city = ""
        self.money = ""
        self.email = ""
        self.name_trans = ""
        self.job = ""

    def gen_name(self, transliterate):
        # Generating a name with faker library
        fake = Faker('bg_BG')
        self.name = fake.name()
        # Splitting the name to remove titles like Dr. and Mr.
        name_lst = self.name.split(" ")
        if len(name_lst) > 2:
            del name_lst[0]
            self.name = " ".join(name_lst)
        # Transliterating the name from cyrillic to latin script with transliterate library
        if transliterate:
            self.name_trans = translit(self.name, 'bg', reversed=True)
            return self.name_trans
        else:
            return self.name

    def generate_birthdate(self):
        # Get the current year
        current_year = datetime.datetime.now().year

        # Generate a random year between 1900 and the current year
        year = random.randint(1900, current_year)

        # Generate a random month between 1 and 12
        month = random.randint(1, 12)

        # Check how many days are in the month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month == 2:
            if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)

        # Generate random hour, minute, and second values
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        # Return the generated birthdate and time
        self.birthdate = datetime.datetime(year, month, day, hour, minute, second)
        return self.birthdate

    def gen_personal_number(self):
        birthdate_lst = str(self.birthdate).split("-")
        year = birthdate_lst[0][2:]
        month = birthdate_lst[1]
        day = birthdate_lst[2][:2]
        self.personal_number += year
        self.personal_number += month
        self.personal_number += day
        for i in range(4):
            self.personal_number += str(random.randint(0, 9))
        return self.personal_number

    def gen_city(self):

        # List of Bulgarian cities
        bulgarian_cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse", "Stara Zagora", "Pleven", "Sliven",
                            "Dobrich", "Shumen", "Pernik", "Haskovo", "Yambol", "Blagoevgrad", "Veliko Tarnovo",
                            "Gabrovo", "Vratsa", "Kardzhali", "Kyustendil", "Montana", "Lovech", "Razgrad", "Silistra",
                            "Targovishte", "Asenovgrad", "Dimitrovgrad", "Dupnitsa", "Gorna Oryahovitsa", "Kazanlak",
                            "Lom", "Nova Zagora", "Petrich", "Popovo", "Samokov", "Sevlievo", "Simitli", "Svilengrad",
                            "Troyan", "Velingrad"]

        # List of the top 50 most populated cities in Europe and North America
        top_cities = ["Moscow", "Istanbul", "Paris", "London", "Madrid", "Barcelona", "Berlin", "Milan", "Rome",
                      "Prague", "Vienna", "Munich", "Amsterdam", "Brussels", "Stockholm", "Copenhagen", "Hamburg",
                      "Minsk", "Warsaw", "Dublin", "Budapest", "Belgrade", "Kiev", "Bucharest", "Athens", "Toronto",
                      "New York City", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio",
                      "San Diego", "Dallas", "San Jose", "Boston", "Washington", "Seattle", "Denver", "Atlanta",
                      "Miami", "Toronto", "Montreal", "Vancouver", "Ottawa", "Calgary", "Edmonton", "Quebec City"]

        # Randomly choose a city
        if random.random() < 0.05:
            # 5% chance of returning a top city
            city = random.choice(top_cities)
        else:
            # 95% chance of returning a Bulgarian city
            city_weights = [0.35, 0.2, 0.15, 0.15, 0.15]  # weights for the first 5 Bulgarian cities
            city_weights.extend([0.05] * (len(bulgarian_cities) - 5))  # equal weights for the rest of the cities
            city = random.choices(bulgarian_cities, weights=city_weights)[0]

        self.city = city
        return self.city

    def gen_wealth(self):
        mean = 10.0  # equivalent to $10,000
        stddev = 0.5

        # generate a random bank balance based on the log-normal distribution
        bank_balance = np.exp(random.normalvariate(mean, stddev))

        self.money = "Bank balance: ${:.2f}".format(bank_balance)
        return self.money

    def gen_mail(self):
        domains = ['abv.bg', 'gmail.com', 'mail.bg', 'yahoo.com', 'hotmail.com']
        names = self.name_trans.split(" ")
        for i in range(len(names)):
            self.email += names[i].lower()
            if names[i] != names[-1]:
                self.email += "."
        self.email += "@"
        domain_seed = random.randint(0, 10)
        if 0 <= domain_seed < 6:
            self.email += domains[1]
        elif 6 <= domain_seed < 8:
            self.email += domains[0]
        else:
            self.email += domains[random.randint(2, 4)]
        return self.email

    def gen_job(self):
        professions = ['accountant', 'architect', 'chef',
                       'dentist', 'engineer', 'financial analyst',
                       'graphic designer', 'human resources manager',
                       'journalist', 'lawyer', 'marketing manager',
                       'nurse', 'pharmacist', 'physician', 'programmer',
                       'real estate agent', 'sales representative',
                       'teacher', 'veterinarian', 'web developer']

        random_profession = random.choice(professions)
        self.job = random_profession
        return self.job




