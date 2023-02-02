from faker import Faker
from transliterate import translit


def gen_name(transliterate):
    # Generating a name with faker library
    fake = Faker('bg_BG')
    name = fake.name()
    # Splitting the name to remove titles like Dr. and Mr.
    name_lst = name.split(" ")
    if len(name_lst) > 2:
        del name_lst[0]
        name = " ".join(name_lst)
    # Transliterating the name from cyrillic to latin script with transliterate library
    if transliterate:
        name_trans = translit(name, 'bg', reversed=True)
        return name_trans
    else:
        return name
# Set variable to true if you want to transliterate the name


var_trans = True
print(gen_name(var_trans))
