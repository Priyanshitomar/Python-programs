rows1, cols1 = map(int, input("Enter rows and columns for matrix1: ").split())
rows2, cols2 = map(int, input("Enter rows and columns for matrix2: ").split())
if cols1 != rows2:
    print("Multiplication not possible")
else:
    matrix1 = [[int(input(f"Matrix1 [{i}][{j}]: ")) for j in range(cols1)] for i in range(rows1)]
    matrix2 = [[int(input(f"Matrix2 [{i}][{j}]: ")) for j in range(cols2)] for i in range(rows2)]
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("Resultant Matrix:", result)
