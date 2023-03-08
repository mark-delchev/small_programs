import random
import math

mean = (45 + (-32)) / 1.6
std_dev = 10

while True:
    degrees_C = round(random.normalvariate(mean, std_dev))
    degrees_F = math.floor(degrees_C * 9 / 5 + 32)
    degrees_K = math.floor(degrees_C + 273.15)
    if -32 <= degrees_C <= 45:
        break


print(f"{degrees_C} C")
print(f"{degrees_F} F")
print(f"{degrees_K} K")
