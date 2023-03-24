values_lst = [int(i) for i in input().split(" ")]
a = values_lst[0]
b = values_lst[1]
c = values_lst[2]

if a > 0 and b > 0 and c > 0:
    print(f"Equation: {a}x^2 + {b}x + {c}")
elif b < 0:
    print(f"Equation: {a}x^2 - {-b}x + {c}")
elif c < 0:
    print(f"Equation: {a}x**2 + {b}x - {-c}")

d = b ** 2 - 4 * a * c
print(d)
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1, x2)

elif d == 0:
    x1 = -b / 2
    print(x1)

else:
    print("Discriminant is negative")
