

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

# More optimized version


def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


number = int(input())
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

