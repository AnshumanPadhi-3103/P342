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

def f_prime(f, x ): #function to find the 1st derivative of a function
    h = 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)
def f_double_prime(f, x): #function to find the 1st derivative of a function
    h = 0.0001
    return (f(x + h) + f(x - h) - 2 * f(x)) / (h ** 2)

def Bracketing(f,a,b): #providing guesses for the interval and bracketing the root
    product= f(a)*f(b)
    if product<0: #if the product is negative it implies the solution lies between a and b
        print("Root already exists in the guessed interval")
        return a,b
    else:
        i = 0
        while product>0: #if the product is positive hence both f(a) and f(b) lie on the same side
            if abs(f(a))<abs(f(b)): #means solution is to the left
                a=a- 1.5*(b-a) #Defining a new 'a' to its left
                product = f(a) * f(b)
                i=i+ 1
            else:
                b = b + 1.5 * (b - a) #means solution is to the right
                product = f(a) * f(b) #Defining a new 'b' to its right
                i=i+ 1
        print("The solution exists in the interval:",a,b)
        return a,b

def Regular_falsi(f,a,b,tol,max_itr):
    #defining all blank lists for future storage
    Iterartion=[]
    Root_val=[]
    error=[]
    c=a #initiating a guess at one of the end points of the bracket
    for i in range(max_itr):
        prev_c=c #storing the previous value
        c = b- (((b - a)*f(b))/(f(b)-f(a)))
        if abs(b-a)<tol: #if a and b are too close to the solution
            continue
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
        if abs(c - prev_c) > tol: #the difference between c and the previous c is the absolute error in this iteration
            #storing no, of iterations, root and absolute error at each iteration in respective lists
            Iterartion.append(i)
            Root_val.append(c)
            e=abs(Root_val[i]-Root_val[i-1])
            error.append(e)
        else: #if the error converges and no significant error is noticed
            return c,Iterartion,Root_val, error



def Bisection(f,a,b,tol,max_itr):
    # defining all blank lists for future storage
    Iterartion=[]
    Root_val=[]
    for i in range(max_itr):
        c = (a+b)/2
        if abs(b - a) < tol: #if a and b are too close to the solution
            continue
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        # storing no, of iterations, root and absolute error at each iteration in respective lists
        Iterartion.append(i)
        Root_val.append(c)


    return c,Iterartion,Root_val

def abs_error(Val): #fucntion to find the absolute error in each iteration
    error=[]
    for i in range(len(Val)-1):
        q= abs(Val[i+1]-Val[i]) # |c_{i+1}-c_{i}|
        error.append(q)
    return error
def Newton_Raphson(f,b,tol,max_itr):
    # defining all blank lists for future storage
    Iterartion = []
    Root_val = []
    for i in range(max_itr):
        c = b - (f(b)/f_prime(f,b))

        if abs(b-c)>tol:
            b = c
            # storing no, of iterations, root and absolute error at each iteration in respective lists
            Iterartion.append(i)
            Root_val.append(c)
        else:
            return c,Iterartion,Root_val


def poly_f(A, x): #fucntion for intaking coefficients of the terms of higher order to lower order and writing a polynomial
    n = len(A)
    sum = 0
    for i in range(n):
        sum = sum + A[i] * x**(n-1-i) #since n-1 would be the order of polynomial
    return sum

def poly_prime(A, x ): #fucntion to find the prime of a polynomial
    h=0.0001
    return (poly_f(A, x+h) - poly_f(A, x-h))/(2*h)

def poly_double_prime(A, x): #fucntion to find the double prime of a polynomial
    h = 0.0001
    return (poly_f(A, x+h) + poly_f(A, x-h) - 2 * poly_f(A, x)) / (h ** 2)

def laguerre(A, b, tol): #fucntion for laguerre's method of finding root, intakes coefficients (higher-lower) and a guess value
    for i in range(200):
        if abs(poly_f(A, b)) < tol: #guessed value is the solution
            return b
        else:
            G = poly_prime(A, b)/(poly_f(A, b)) #defining G= f'(b)/f(b)
            K= (poly_double_prime(A, b)/poly_f(A, b)) #defining P= f''(b)/f(b)
            H = G**2 - K
            n = len(A) - 1 #order of polynomial
            # statement used to maximise the denominator of a = n / (G +/- ((n - 1) * (n * H - G**2)) ** 0.5)
            if G>=0:
                a = n/(G + ((n-1)*(n*H - G**2))**0.5)
            else:
                a = n/(G - ((n-1)*(n*H - G**2))**0.5)
            b0=b
            b = b - a
            if abs(b - b0) < tol: #stopping iteration if 'b' converges
                return b0


def syn_div(A, b,tol): #dividing a polynomial with coefficient list A with x-b
    n=len(A)
    q = [] #creating blank list for future storage of the reduced polynomial
    q.append(A[0])
    for i in range(1, n):
        q.append(b*q[i-1] + A[i])
    if q[n-1]>tol: #checking if the remainder value is ignorable or not
        print("Polynomial not divisible ",q[n])
    else: q.pop() #if not, excluding it from the list
    return q

