from Library import Bracketing,Bisection,abs_error #importing desired functions
import math

def f(x):
    return -x-math.cos(x)



def table_making(Iter, Val, convergence): #defining a function for exporting the data to a txt file
    n=len(convergence)
    A = [[0 for j in range(3)] for i in range(n)]
    f = open('1b.Bisection.txt', 'w')
    for i in range(n):
        for j in range(3):
            A[i][:] = [Iter[i], Val[i], convergence[i]]

        f.writelines(str(A[i])[1:-1] + "\n")
    f.close()

    return A

max_iteration=200 #defining max number of allowed iterations
a,b=Bracketing(f,4.6,5.13) #providing guesses for the interval and bracketing the root

soln,Iter,Val=Bisection(f,a,b,10**-6,max_iteration) #finding the solution to the equation, and the lists for number of iterations and the value of the root obtained at each iteration
convergence=abs_error(Val) #finding the list for absolute error in each iterations
print("Solution is:",soln)
print("Itr. No.|","Root Value|","Absolute Error")
A = table_making(Iter, Val, convergence) #exporting the no. of iterations, root values and absolute error to a txt file


#printing the file in terminal
file1 = open('1b.Bisection.txt', 'r')
print(file1.read())
file1.close()


#C:\Users\Anshuman\PycharmProjects\pythonProject1\venv\Scripts\python.exe C:/Users/Anshuman/PycharmProjects/pythonProject1/main.py
#The solution exists in the interval: -3.1512500000000045 5.13
#Solution is: -0.7390847735852035
#Itr. No.| Root Value| Absolute Error
#0, 0.9893749999999977, 2.070312500000001
#1, -1.0809375000000034, 1.0351562500000004
#2, -0.04578125000000288, 0.5175781250000003
#3, -0.5633593750000032, 0.2587890625000001
#4, -0.8221484375000033, 0.1293945312500001
#5, -0.6927539062500032, 0.064697265625
#6, -0.7574511718750032, 0.0323486328125
#7, -0.7251025390625032, 0.01617431640625
#8, -0.7412768554687532, 0.008087158203125
#9, -0.7331896972656282, 0.0040435791015625
#10, -0.7372332763671907, 0.00202178955078125
#11, -0.739255065917972, 0.001010894775390625
#12, -0.7382441711425813, 0.0005054473876953125
#13, -0.7387496185302767, 0.00025272369384765625
#14, -0.7390023422241243, 0.00012636184692382812
#15, -0.7391287040710481, 6.318092346191406e-05
#16, -0.7390655231475862, 3.159046173095703e-05
#17, -0.7390971136093172, 1.5795230865478516e-05
#18, -0.7390813183784517, 7.897615432739258e-06
#19, -0.7390892159938844, 3.948807716369629e-06
#20, -0.7390852671861681, 1.9744038581848145e-06
#21, -0.7390832927823099, 9.872019290924072e-07


#Process finished with exit code 0
