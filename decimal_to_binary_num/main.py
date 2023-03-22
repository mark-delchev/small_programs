
bits = int(input('Enter the number of bits you want in your number: '))

while True:
    num = int(input(f'Enter a number between 0 and {2 ** bits - 1}: '))
    if 2 ** bits >= num > 0:
        break
    else:
        print("Invalid num")

binary_num = ""
power = bits - 1
for i in range(bits):
    if num >= 2 ** (power - i):
        binary_num += "1"
        num -= 2 ** (power - i)
    else:
        binary_num += "0"

print(binary_num)


