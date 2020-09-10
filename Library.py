
def PartialPivot(AugM,n,m):

    for r in range(n-1): #running loop till 2nd last column
        if AugM[r][r] == 0: #for a diagonal element 0
            for i in range(r + 1, n):
                if abs(AugM[i][r]) > AugM[r][r]: #if the next row(s) are greater than 0
                    for c in range(r, m): #selcting that row
                        AugM[r][c], AugM[i][c] = AugM[i][c], AugM[r][c] #swapping it with the row with diagonal element 0
                        continue
    print('Matrix after partial pivot:')
    print_arrays(AugM)
    return AugM

def GaussJordan(AugM,n):

    for r in range(n):
        PartialPivot(AugM)
        # for making the pivots = 1
        piv = AugM[r][r]
        for c in range(r, 2*n):
            AugM[r][c] /= piv

        # for making the rest of the column except the pivot = 0
        for i in range(n):
            if i == r or AugM[i][r] == 0:
                continue
            else:
                factor = AugM[i][r]
                for c in range(r, 2*n):
                    AugM[i][c] -= factor * AugM[r][c]
    return AugM

def print_arrays(p):
    print('\n'.join([''.join(['{0:8}'.format(round(item, 3)) for item in row]) for row in p]))
    return p

def print_imported_matrix(C):
    M = [[int(num) for num in line.split(',')] for line in C]
    print("The Matrix: ")
    print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in M]))
    return M


def sum_till_n(n):
    if n<0:
        print("Invalid Input! Enter a positive Integer!")
    else:
        sum=0
        for i in range(n+1):
            sum=sum+i
    print('1+2+3.....+n=')
    print(sum)
    return sum

def fact_n(n):
    if n<0:
        print("Invalid Input! Enter a positive Integer!")
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
    print('n!=')
    print(fact)
    return fact

def Add_vector(a,b,n):
    add = []
    for i in range(n):
        add.append(a[i] + b[i])
    print('Sum of the vectors=')
    print(add)
    return add

def dotproduct(a,b,n):
    prod=0
    for i in range(n):
        prod+= a[i]*b[i]
    return prod



def Multiply(M,N,n): #for multiplying squared matrix
    MN = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                MN[i][j] += M[i][k] * N[k][j]
    print_arrays(MN)
    return MN

def Identity_Aug(M): #for augmenting an Identity matrix with a given matrix
    n=len(M)
    AugM= [[0 for j in range(2*n)] for i in range(n)]
    for j in range(n):
        for i in range(n):
            AugM[i][j]=M[i][j]
    for j in range(n+1,2*n):
        for i in range(n):
            k= i + n
            AugM[i][k]= 1
    print('The Augmented Matrix:')
    print_arrays(AugM)
    return AugM

def lu_decomposition(A, n):
    # Create blank matrices for L and U
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for j in range(n):  # running loop across column

        L[j][j] = 1  # assigning 1 in every diagonal element of A

        for i in range(j + 1):  # running loop from 1st to jth row
            s1 = 0
            for k in range(i):
                s1 += U[k][j] * L[i][k]  # k_sum
            U[i][j] = A[i][j] - s1  # Defining terms of the U matrix
            A[i][j] = U[i][j]  # Storing terms of U in the original

        for i in range(j + 1, n):  # running loop for the rest of the rows
            s2 = 0
            for k in range(i):
                s2 += U[k][j] * L[i][k]  # k_sum
            L[i][j] = (A[i][j] - s2) / U[j][j]  # Defining terms of the L matrix
            A[i][j] = L[i][j]  # Storing terms of L in the original
    # printing the results
    print('L Matrix after LU Decomposition:')
    print_arrays(L)
    print('U Matrix after LU Decomposition:')
    print_arrays(L)
    print('Storing L and U in A itself:')
    print_arrays(L)
    return (L, U, A)

def forward_backward(a, b, n):
    #forward substitution
    for i in range(n):  # running loop through all rows
        for j in range(i):  # for j<i
            b[i] = b[i] - a[i][j] * b[j] #applying formulae
    # backward substitution
    for i in range(n - 1, -1, -1):  # running decreasing loop from  from nth to 1st row
        for j in range(i + 1, n):  # i<j(as U is upper triangular)
            b[i] = b[i] - a[i][j] * b[j]
        b[i] = b[i] / a[i][i] #applying formulae

    return b

def check_inverse_exists(A):
    n= len(A)
    det=1
    for i in range(n):
        det = det * A[i][i]
    if det==0:
        print('Inverse Does not exist!')
    else:
        print('Inverse exists')
        print('The Determinant value:',det)

    return det

def check_inverse_exists_and_calculate(A):  # function to check if inverse exists, and if so, calculate it
    n = len(A)
    det = 1
    for i in range(n):
        det = det * A[i][i]  # multiplying the diagonal elements
    if det == 0:  # since for a inverse to exist, det!=0
        print('Inverse Does not exist!')
    else:
        print('Inverse exists!')
        print('The Determinant value:', det)
        Inverse_calculate(A, n)  # fucntion to calculate matrix
    return Inverse_calculate(A, n)

def Inverse_calculate(Piv_AugM, n):
    # Creating Blank Matrices and vectors
    A = [[0 for j in range(n)] for i in range(n)]
    inverse_A = [[0 for j in range(n)] for i in range(n)]
    B = [0 for i in range(n)]

    # extracting A from the augmented matrix
    for j in range(n):
        for i in range(n):
            A[i][j] = Piv_AugM[i][j]

    L, U, C = lu_decomposition(A, 4)  # LU decomposition on A
    for i in range(n):  # extracting the columns of pivoted identity matrix
        for j in range(n):
            B[j] = Piv_AugM[j][i + n]
            forward_backward(C, B, n)  # performing forward-backward substitution
        for j in range(n):
            inverse_A[j][i] = B[j] #storing the solution columnwise
    print('The inverse of A:')
    print_arrays(inverse_A)
    return inverse_A










