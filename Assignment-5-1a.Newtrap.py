from Library import Bracketing,Newton_Raphson,abs_error
import math

def f(x):
    return math.log(x)-math.sin(x) #defining the function given in Question 1(a)

def table_making(Iter, Val, convergence):
    n = len(convergence)
    A = [[0 for j in range(3)] for i in range(n)]
    f = open('1a.Newtrap.txt', 'w')
    for i in range(n):
        for j in range(3):
            A[i][:] = [Iter[i], Val[i], convergence[i]]

        f.writelines(str(A[i])[1:-1] + "\n")
    f.close()

    return A



max_iteration=200 #defining max number of allowed iterations
a,b=Bracketing(f,1.5,2.5) #providing guesses for the interval and bracketing the root

soln,Iter,Val=Newton_Raphson(f,b,10**-6,max_iteration) #finding the solution to the equation, and the lists for number of iterations, the value of the root obtained at each iteration, and the absolute error at each iteration
convergence=abs_error(Val)
print("Solution is:",soln)
print("Itr. No.|","Root Value|","Absolute Error")
A = table_making(Iter, Val, convergence)#exporting the no. of iterations, root values and absolute error to a txt file


#printing the file in terminal
file1 = open('1a.Newtrap.txt', 'r')
print(file1.read())
file1.close()

#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#Root already exists in the guessed interval
#Solution is: 2.219107148913746
#Itr. No.| Root Value| Absolute Error
#0, 2.2354033406557887, 0.01622264427200948
#1, 2.2191806963837792, 7.354594655595292e-05


#Process finished with exit code 0
