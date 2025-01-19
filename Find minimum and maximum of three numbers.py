def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)
a, b, c = map(int, input("Enter three numbers: ").split())
minimum, maximum = min_max(a, b, c)
print("Minimum:", minimum, "Maximum:", maximum)
