arr = list(map(int, input("Enter array elements: ").split()))
index = int(input("Enter index to modify: "))
value = int(input("Enter new value: "))
if 0 <= index < len(arr):
    arr[index] = value
    print("Modified Array:", arr)
else:
    print("Index out of range.")
