
# At least one special char 33 to 47, 58 to 64, 91 to 96, 123 to 126

# ASCII range of uppercase letters
valid_range = tuple(range(33, 127))
uppercase_range = tuple(range(65, 91))
number_range = tuple(range(48, 58))
special_range_1 = tuple(range(33, 48))
special_range_2 = tuple(range(58, 65))
special_range_3 = tuple(range(91, 97))
special_range_4 = tuple(range(123, 127))


while True:
    valid_pass = True
    password = input()
    # Converts password to a list of numbers on the ASCII table
    password_ord = [ord(i) for i in password]

    valid_check = [i for i in password_ord if i not in valid_range]
    uppercase_check = [i for i in uppercase_range if i in password_ord]
    number_check = [i for i in number_range if i in password_ord]
    special_check_1 = [i for i in special_range_1 if i in password_ord]
    special_check_2 = [i for i in special_range_2 if i in password_ord]
    special_check_3 = [i for i in special_range_3 if i in password_ord]
    special_check_4 = [i for i in special_range_4 if i in password_ord]

    if len(valid_check) > 0:
        print("invalid characters")
        valid_pass = False
    if len(password) < 8:
        print("password must be at least 8 characters")
        valid_pass = False
    if len(uppercase_check) == 0:
        print("password must include at least one uppercase")
        valid_pass = False
    if len(number_check) == 0:
        print("password must include at least one number")
        valid_pass = False
    if len(special_check_1) == 0 and len(special_check_2) == 0 and \
            len(special_check_3) == 0 and len(special_check_4) == 0:
        print("password must include at least one special character")
        valid_pass = False
    if valid_pass:
        print("password is valid")
        break
    else:
        continue


