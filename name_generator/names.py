from faker import Faker
from transliterate import translit


class Names:
    def __init__(self):
        self.name = ""

    def gen_name(self, locale):
        fake = Faker(locale)
        self.name = fake.name()

        return self.name

