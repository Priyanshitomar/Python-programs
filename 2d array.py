rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
matrix = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
print("2D Array:", matrix)
