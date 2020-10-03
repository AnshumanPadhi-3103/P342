from Library import Bracketing,Regular_falsi
import math

def f(x):
    return -x-math.cos(x)


def table_making(Iter, Val, convergence): #defining a function for exporting the data to a txt file
    n=len(convergence)
    A = [[0 for j in range(3)] for i in range(n)]
    f = open('1b.Regfalsi.txt', 'w')
    for i in range(n):
        for j in range(3):
            A[i][:] = [Iter[i], Val[i], convergence[i]]

        f.writelines(str(A[i])[1:-1] + "\n")
    f.close()

    return A

max_iteration=200 #defining max number of allowed iterations
a,b=Bracketing(f,4.6,5.13) #providing guesses for the interval and bracketing the root

soln,Iter,Val,convergence=Regular_falsi(f,a,b,10**-6,max_iteration) #finding the solution to the equation, and the lists for number of iterations, the value of the root obtained at each iteration, and the absolute error at each iteration
print("Solution is:",soln)
print("Itr. No.|","Root Value|","Absolute Error")
A = table_making(Iter, Val, convergence)#exporting the no. of iterations, root values and absolute error to a txt file

#printing the file in terminal
file1 = open('1b.Regfalsi.txt', 'r')
print(file1.read())
file1.close()

#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#The solution exists in the interval: -3.1512500000000045 5.13
#Solution is: -0.7390851173520689
#Itr. No.| Root Value| Absolute Error
#0, 0.39762261301690405, 0.0
#1, -0.4583962017675641, 0.8560188147844682
#2, -0.7156007988138697, 0.2572045970463056
#3, -0.7383270893994411, 0.022726290585571407
#4, -0.7390641668670821, 0.0007370774676409564
#5, -0.7390845564645103, 2.0389597428227546e-05


#Process finished with exit code 0
