

number = int(input())
dividing_numbers = 0
for i in range(1, number + 1):
    if number % i == 0:
        dividing_numbers += 1
    if dividing_numbers > 2:
        print(f"{number} is not a prime number.")
        break

else:
    print(f"{number} is a prime number.")
