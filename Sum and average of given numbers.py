numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total, "Average:", average)
