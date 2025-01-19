def sum_even_odd(e1, e2, o1, o2):
    return e1 + e2 + o1 + o2
e1, e2, o1, o2 = map(int, input("Enter two even and two odd numbers: ").split())
print("Sum:", sum_even_odd(e1, e2, o1, o2))
