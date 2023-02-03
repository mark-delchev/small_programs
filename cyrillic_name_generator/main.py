from faker import Faker
from transliterate import translit


class NameGen:
    def __init__(self):
        self.name = ""

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
# Set variable to true if you want to transliterate the name
# var_trans = True
