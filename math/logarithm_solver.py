nums = [int(i) for i in input().split(" ")]
a = nums[0]
b = nums[1]
c = nums[2]
constant_e = 2.71828


def logarithm(base, x):
    """
    Computes the logarithm of x with a given base.
    """
    result = 0
    while x >= base:
        x /= base
        result += 1
    return result


print(f"Log{a}_{b}**{c}")
solution = c * logarithm(a, b)
print(solution)