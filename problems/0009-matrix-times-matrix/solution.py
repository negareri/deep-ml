def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1
        
    
    c = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            answer = 0

            for k in range(len(b)):
                answer += a[i][k] * b[k][j]

            row.append(answer)

        c.append(row)
        
    return c