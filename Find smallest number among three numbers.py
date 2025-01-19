def smallest(a, b, c):
    return min(a, b, c)
a, b, c = map(int, input("Enter three numbers: ").split())
print("Smallest:", smallest(a, b, c))
