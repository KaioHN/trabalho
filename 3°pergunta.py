matrixA = [[2, -1],[3,0],[1, 2]]
matrixB = [[1, 0, 4],[-2, 5, 1]]

AxB = [[0,0,0] for c in range(len(matrixA))]
for i in range(len(matrixA)):
    for j in range(len(matrixB)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):  
                 AxB[i][j] += matrixA[i][k] * matrixB[k][j]


print("Resultado da multiplicação A * B:")
for linha in AxB:
    print(linha)

        





