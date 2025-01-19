def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
a, b = map(int, input("Enter two numbers: ").split())
op = input("Enter operation (+, -, *): ")
print("Result:", calculate(a, b, op))
