rows = int(input("Enter number of rows: "))
jagged_array = []
for i in range(rows):
    jagged_array.append(list(map(int, input(f"Enter elements for row {i+1}: ").split())))
print("Jagged Array:", jagged_array)
