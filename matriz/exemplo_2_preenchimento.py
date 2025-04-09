mat = []
for i in range(4):
    mat.append([0] * 5)

'''
mat[0][0] = 1
mat[0][1] = 2
mat[0][2] = 3
mat[0][3] = 4
mat[0][4] = 5
'''
num = 1
for j in range(4):
    for i in range(5):
        mat[j][i] = num
        num = num + 1

for lin in mat:
    print(lin)