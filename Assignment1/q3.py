
def transpose_op(m):

    for row in m : 
        print(row) 
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
    print("\n") 
    for row in rez: 
        print(row) 
    return rez


def upright_diag(x):
    
    res = []
    dup = x[:]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if i < j:
                #res.append(x[i][j])
                dup[i][j] = 0
                
    return dup

def lowleft_diag(mat):

    n = len(mat)
    res = []
    dup = mat[:]
    print("Secondary Diagonal: ", end = "")
 
    for i in range(n):
        for j in range(n):
 
            # Condition for secondary diagonal
            #if ((i + j) == (n - 1)):
            #    res.append(mat[i][j])
            if i > j:
                #res.append(x[i][j])
                dup[i][j] = 0                

    return dup


def rotate90Clockwise(a):
    N = len(a[0])
    for i in range(N // 2):
        for j in range(i, N-i-1):
            temp = a[i][j]
            a[i][j] = a[N-1-j][i]
            a[N - 1 - j][i] = a[N - 1 - i][N - 1 - j]
            a[N - 1 - i][N - 1 - j] = a[j][N - 1 - i]
            a[j][N - 1 - i] = temp
    return a