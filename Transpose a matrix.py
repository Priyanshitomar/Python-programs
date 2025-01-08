rows, cols = map(int, input("Enter rows and columns: ").split())
matrix = [[int(input(f"Matrix [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
print("Transpose:", transpose)
