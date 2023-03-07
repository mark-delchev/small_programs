import random
import math

degrees_C = random.randint(-32, 45)
degrees_F = math.floor(degrees_C * 9 / 5 + 32)
print(f"{degrees_C} C")
print(f"{degrees_F} F")
