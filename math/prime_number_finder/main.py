import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(123127))