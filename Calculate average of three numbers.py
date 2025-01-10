def average(a, b, c):
    return (a + b + c) / 3
a, b, c = map(int, input("Enter three numbers: ").split())
print("Average:", average(a, b, c))
