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
    # forward substitution
    for i in range(n):  # running loop through all rows
        for j in range(i):  # for j<i
            b[i] = b[i] - a[i][j] * b[j]  # applying formulae
    # backward substitution
    for i in range(n - 1, -1, -1):  # running decreasing loop from  from nth to 1st row
        for j in range(i + 1, n):  # i<j(as U is upper triangular)
            b[i] = b[i] - a[i][j] * b[j]
        b[i] = b[i] / a[i][i]  # applying formulae

    return b


def extract_A_B(Piv_AugM, n):  # function to extract A from pivoted matrix
    A = [[0.0 for j in range(n)] for i in range(n)]
    for j in range(n):
        for i in range(n):
            A[i][j] = Piv_AugM[i][j]

    return A


def check_inverse_exists_and_calculate(A, Piv_AugM):  # function to check if inverse exists, and if so, calculate it
    n = len(A)
    L, U, A = lu_decomposition(A, n)  # Performing LU Decomposition
    # Calculating determinant of the decomposed matrix
    det = 1
    for i in range(n):
        det = det * A[i][i]  # multiplying the diagonal elements
    # for checking whether matrix is invertible or not
    if det == 0:  # since for a inverse to exist, det!=0
        print('Inverse Does not exist!')
    else:
        print('Inverse exists!')
        print('The Determinant value:', det)
        inverse_A = [[0 for j in range(n)] for i in range(n)]
        # extracting B coulumn-wise and using it in forward backward substitution
        for i in range(n):
            B = [0.0 for i in range(n)]
            for j in range(n):
                B[j] = Piv_AugM[j][i + n]

            B = forward_backward(A, B, n)
            for j in range(n):  # Storing B in as inverse matrix coulmnwise
                inverse_A[j][i] = B[j]
        print('The Inverse is:')
        print_arrays(inverse_A)
        return inverse_A


# calling and printing the matrix
F = open('InvA.txt', 'r')
D = print_imported_matrix(F)

AugM = Identity_Aug(D)  # Augmenting it with Identity matrix of same order

Pivoted_AugM = PartialPivot(AugM, 4, 8)  # partial pivoting the augmented matrix
A = extract_A_B(Pivoted_AugM, 4)
p = check_inverse_exists_and_calculate(A, Pivoted_AugM)  # function to check if inverse exists, and if so, calculate it

# C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
# The Matrix:
#     0     2     8     6
#     0     0     1     2
#     0     1     0     1
#     3     7     1     0
# The Augmented Matrix:
#       0       2       8       6       1       0       0       0
#       0       0       1       2       0       1       0       0
#       0       1       0       1       0       0       1       0
#       3       7       1       0       0       0       0       1
# Matrix after partial pivot:
#       3       7       1       0       0       0       0       1
#       0       2       8       6       1       0       0       0
#       0       0       1       2       0       1       0       0
#       0       1       0       1       0       0       1       0
# Inverse exists!
# The Determinant value: 36.0
#   -0.25   1.667  -1.833   0.333
#   0.083  -0.667   0.833     0.0
#   0.167  -0.333  -0.333     0.0
#  -0.083   0.667   0.167     0.0

# Process finished with exit code 0

