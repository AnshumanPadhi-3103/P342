from Library import  print_imported_matrix, print_arrays

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




F = open('A.txt', 'r') #Calling the txt file for LHS matrix
D= print_imported_matrix(F) #arranging and printing

G = open('B.txt','r') #calling the txt file for RHS vector
M= [int(num) for num in G] #arranging it in form of an array

L,U,A=lu_decomposition(D,4) #Decomposing the called LHS matrix
X=forward_backward(A,M,4) #Running forward Backward substitution
print('The solution obtained after forward-backward substitution:')
print(X) #result


#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#The Matrix:
#     1     0     1     2
#     0     1    -2     0
#     1     2    -1     0
#     2     1     3    -2
#L Matrix after LU Decomposition:
#       1     0.0     0.0     0.0
#     0.0       1     0.0     0.0
#     1.0     2.0       1     0.0
#     2.0     1.0     1.5       1
#U Matrix after LU Decomposition:
#       1     0.0     0.0     0.0
#     0.0       1     0.0     0.0
#     1.0     2.0       1     0.0
#     2.0     1.0     1.5       1
#Storing L and U in A itself:
#       1     0.0     0.0     0.0
#     0.0       1     0.0     0.0
#     1.0     2.0       1     0.0
#     2.0     1.0     1.5       1
#The solution obtained after forward-backward substitution:
#[1.0, -1.0, 1.0, 2.0]

#Process finished with exit code 0



