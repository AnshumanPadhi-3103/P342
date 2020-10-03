from Library import Bracketing,Bisection,abs_error #importing desired functions
import math

def f(x):
    return math.log(x)-math.sin(x) #defining the function given in Question 1(a)

def table_making(Iter, Val, convergence): #defining a function for exporting the data to a txt file
    n=len(convergence)
    A = [[0 for j in range(3)] for i in range(n)]
    f = open('1a.Bisection.txt', 'w')
    for i in range(n):
        for j in range(3):
            A[i][:] = [Iter[i], Val[i], convergence[i]]

        f.writelines(str(A[i])[1:-1] + "\n")
    f.close()

    return A

max_iteration=200 #defining max number of allowed iterations
a,b=Bracketing(f,1.5,2.5) #providing guesses for the interval and bracketing the root

soln,Iter,Val=Bisection(f,a,b,10**-6,max_iteration) #finding the solution to the equation, and the lists for number of iterations and the value of the root obtained at each iteration
convergence=abs_error(Val) #finding the list for absolute error in each iterations
print("Solution is:",soln)
print("Itr. No.|","Root Value|","Absolute Error")
A = table_making(Iter, Val, convergence) #exporting the no. of iterations, root values and absolute error to a txt file


#printing the file in terminal
file1 = open('1a.Bisection.txt', 'r')
print(file1.read())
file1.close()


#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#Root already exists in the guessed interval
#Solution is: 2.219107151031494
#Itr. No.| Root Value| Absolute Error
#0, 2.0, 0.25
#1, 2.25, 0.125
#2, 2.125, 0.0625
#3, 2.1875, 0.03125
#4, 2.21875, 0.015625
#5, 2.234375, 0.0078125
#6, 2.2265625, 0.00390625
#7, 2.22265625, 0.001953125
#8, 2.220703125, 0.0009765625
#9, 2.2197265625, 0.00048828125
#10, 2.21923828125, 0.000244140625
#11, 2.218994140625, 0.0001220703125
#12, 2.2191162109375, 6.103515625e-05
#13, 2.21905517578125, 3.0517578125e-05
#14, 2.219085693359375, 1.52587890625e-05
#15, 2.2191009521484375, 7.62939453125e-06
#16, 2.2191085815429688, 3.814697265625e-06
#17, 2.219104766845703, 1.9073486328125e-06
#18, 2.219106674194336, 9.5367431640625e-07


#Process finished with exit code 0
