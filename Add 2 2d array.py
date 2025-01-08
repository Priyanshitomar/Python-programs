rows, cols = map(int, input("Enter rows and columns: ").split())
array1 = [[int(input(f"Array1 [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
array2 = [[int(input(f"Array2 [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
result = [[array1[i][j] + array2[i][j] for j in range(cols)] for i in range(rows)]
print("Resultant Array:", result)
