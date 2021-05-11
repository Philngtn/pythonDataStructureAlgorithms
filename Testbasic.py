a = [2,54,213,24,42,1,7]
a = [0,1,2,3,4]

b = [[0 for i in range(3)] for j in range(len(a))]


for i in a:
    for j in range(3):
        if j == 0:
            b[i][j] = i
        else:
            b[i][j] = 0
         

print(min(b[:][0]))
