import random
import datetime
from faker import Faker
from transliterate import translit


class Person:
    def __init__(self):
        self.name = ""
        self.birthdate = ""
        self.personal_number = ""

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
            name_trans = translit(self.name, 'bg', reversed=True)
            return name_trans
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
