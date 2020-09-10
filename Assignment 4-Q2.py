from Library import PartialPivot, print_imported_matrix, Identity_Aug, print_arrays

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

#calling and printing the matrix
F = open('InvA.txt', 'r')
D = print_imported_matrix(F)

AugM = Identity_Aug(D) #Augmenting it with Identity matrix of same order
Pivoted_AugM = PartialPivot(AugM, 4, 8) #partial pivoting the augmented matrix

p = check_inverse_exists_and_calculate(Pivoted_AugM) # function to check if inverse exists, and if so, calculate it


#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#The Matrix:
#     0     2     8     6
#     0     0     1     2
#     0     1     0     1
#     3     7     1     0
#The Augmented Matrix:
#       0       2       8       6       1       0       0       0
#       0       0       1       2       0       1       0       0
#       0       1       0       1       0       0       1       0
#       3       7       1       0       0       0       0       1
#Matrix after partial pivot:
#       3       7       1       0       0       0       0       1
#       0       2       8       6       1       0       0       0
#       0       0       1       2       0       1       0       0
#       0       1       0       1       0       0       1       0
#Inverse exists!
#The Determinant value: 6
#The inverse of A:
#   0.101   0.173  -1.882   -0.12
#  -0.033   0.165   0.857   0.063
#  -0.024  -0.002  -0.317   0.037
#   0.033  -0.165   0.143  -0.063
#The inverse of A:
#   0.101   0.173  -1.882   -0.12
#  -0.033   0.165   0.857   0.063
#  -0.024  -0.002  -0.317   0.037
#   0.033  -0.165   0.143  -0.063

#Process finished with exit code 0

