num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
if sum(d**len(digits) for d in digits) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
