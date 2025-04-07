li = [[1, 2, 3],[4, 5, 6],[2,7,5]]
result = [[0,0,0], [0,0,0],[0,0,0]]
for i in range(len(li)):
    for j in range(len(li[0])):
        result[j][i]=li[i][j]
for r in result:
    print(r)
