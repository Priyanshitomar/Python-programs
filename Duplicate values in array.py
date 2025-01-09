arr = list(map(int, input("Enter array elements: ").split()))
duplicates = [x for x in set(arr) if arr.count(x) > 1]
print("Duplicate values:", duplicates)
