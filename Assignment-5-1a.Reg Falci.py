from Library import Bracketing,Regular_falsi
import math

def f(x):
    return math.log(x)-math.sin(x)

def table_making(Iter, Val, convergence): #defining a function for exporting the data to a txt file
    n=len(convergence)
    A = [[0 for j in range(3)] for i in range(n)]
    f = open('1a.Regfalsi.txt', 'w')
    for i in range(n):
        for j in range(3):
            A[i][:] = [Iter[i], Val[i], convergence[i]]

        f.writelines(str(A[i])[1:-1] + "\n")
    f.close()

    return A



max_iteration=200 #defining max number of allowed iterations
a,b=Bracketing(f,1.5,2.5) #providing guesses for the interval and bracketing the root

soln,Iter,Val,convergence=Regular_falsi(f,a,b,10**-6,max_iteration) #finding the solution to the equation, and the lists for number of iterations, the value of the root obtained at each iteration, and the absolute error at each iteration
print("Solution is:",soln)
print("Itr. No.|","Root Value|","Absolute Error")
A = table_making(Iter, Val, convergence)#exporting the no. of iterations, root values and absolute error to a txt file

#printing the file in terminal
file1 = open('1a.Regfalsi.txt', 'r')
print(file1.read())
file1.close()



#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#Root already exists in the guessed interval
#Solution is: 2.2191071418525734
#Itr. No.| Root Value| Absolute Error
#0, 2.150690637448136, 0.0
#1, 2.214278807270502, 0.06358816982236615
#2, 2.218777764768144, 0.004498957497641953
#3, 2.2190847331897734, 0.0003069684216292501
#4, 2.219105623699575, 2.0890509801585466e-05
#5, 2.2191070451360577, 1.4214364827402903e-06


#Process finished with exit code 0
