def add_numbers(a, b):
    return a + b
a, b = map(int, input("Enter two numbers: ").split())
print("Sum:", add_numbers(a, b))
