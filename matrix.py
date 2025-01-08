rows, cols = map(int, input("Enter rows and columns: ").split())
matrix1 = [[int(input(f"Matrix1 [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
matrix2 = [[int(input(f"Matrix2 [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("Resultant Matrix:", result)
